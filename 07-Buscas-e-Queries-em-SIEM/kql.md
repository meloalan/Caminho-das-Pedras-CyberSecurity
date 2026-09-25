# KQL: tabelas, pipelines e contexto de segurança

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](traduzindo-queries.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](spl.md)

## Linguagem e ambiente não são a mesma coisa

Kusto Query Language é a linguagem. SecurityEvent e WindowsEvent são schemas do Azure Monitor usados neste material. Microsoft Defender Advanced Hunting possui tabelas como DeviceProcessEvents com Timestamp, DeviceName e ProcessCommandLine; elas não existem automaticamente num workspace Log Analytics. Não troque apenas o nome da tabela. Sentinel, permissões e conectores determinam a disponibilidade dos dados.

## Operadores preservados e ampliados

| Operador | Uso em segurança | Cuidado |
| --- | --- | --- |
| where | Manter eventos/tempo pertinentes | Filtro pode esconder lacuna de coleta |
| project | Selecionar campos de evidência | Preserve chaves antes de correlacionar |
| extend | Criar coluna ou converter EventData | Conversão inválida pode produzir null |
| summarize / count | Agregar ou contar linhas | Granularidade muda |
| distinct | Combinações únicas | Não demonstra quem nunca enviou dados |
| top / sort | Classificar volume ou horário | Top oculta o restante |
| bin / ago | Intervalo fixo / início relativo | Bin não é sliding window |
| let | Nomear parâmetro ou expressão | Não é garantia de materialização |
| join | Relacionar por chave | Declare kind e examine cardinalidade |
| union | Concatenar conjuntos | Tipos e colunas podem divergir |
| parse | Extrair de formato conhecido | Não substitui entender o schema |
| mv-expand | Abrir array/objeto em linhas | Multiplica linhas e altera contagens |
| make_set | Conjunto de valores distintos | Limite explícito e ordem não garantida |
| arg_max | Linha associada ao máximo | Empates e múltiplas versões exigem critério |

## Exercício sintético de transformação

```kusto
datatable(Host:string, Tags:dynamic, Mensagem:string)
["WIN-LAB01",dynamic(["lab","windows"]),"owner=Lab Team;status=ativo"]
| parse Mensagem with "owner=" Owner ";status=" Estado
| mv-expand Tag=Tags to typeof(string)
| project Host, Tag, Owner, Estado
```

Uma linha contém duas tags, portanto a saída tem duas linhas. parse extrai valores pelo padrão literal; mv-expand abre o array. Contar depois mede tags expandidas, não máquinas. Teste mensagem fora do padrão para perceber campos sem valor.

## Último registro e amostra de valores

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h)
| summarize arg_max(TimeGenerated, EventID, TargetUserName) by Computer
```

Mostra um registro associado ao maior horário por computador. Não é inventário de hosts silenciosos. Se houver empate, não use essa seleção para afirmar qual ação foi realmente a última. Para exemplos de comandos em um hunt, `make_set(CommandLine, 3)` guarda até três valores distintos, sem representar todos os comandos.

## Union exige contrato comum

```kusto
let A=SecurityEvent
| where TimeGenerated >= ago(1h)
| project Tempo=TimeGenerated, Host=Computer, Fonte="Security", ID=EventID;
let B=WindowsEvent
| where TimeGenerated >= ago(1h)
| where Provider == "Microsoft-Windows-Sysmon"
| project Tempo=TimeGenerated, Host=Computer, Fonte="Sysmon", ID=EventID;
union A, B
| order by Tempo asc
```

Cada lado filtra e projeta nomes/tipos comuns. Fonte permanece para não confundir ID 1 de diferentes provedores. A timeline organiza observações; não prova vínculo entre elas.

## Do estudo anterior ao módulo atual

O exercício datatable está em [fundamentos](fundamentos-de-consulta.md). Where/project/extend/count/distinct/top/let/ago foram mantidos em [operadores](operadores-e-transformacoes.md) e nesta referência. Bin e suas fronteiras estão em [tempo](tempo-em-queries.md); innerunique, cardinalidade e leftouter em [correlação](correlacao-e-joins.md). As [seis consultas KQL existentes](../queries/kql/README.md) continuam disponíveis.

## Fontes e prática

[Referência rápida KQL](https://learn.microsoft.com/en-us/kusto/query/kql-quick-reference), [mv-expand](https://learn.microsoft.com/en-us/kusto/query/mv-expand-operator), [arg_max](https://learn.microsoft.com/en-us/kusto/query/arg-max-aggregation-function) e [schema Advanced Hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables) delimitam uso e ambiente.

Execute um exemplo por vez. Anote número de linhas antes/depois de cada operador e explique a mudança sem usar o nome do comando como explicação.

## Checkpoint

**KQL garante que SecurityEvent exista?**

<details>
<summary>Ver resposta</summary>

Não. Linguagem, schema, ingestão e permissão são partes separadas do contrato.

</details>

[← Tópico anterior](traduzindo-queries.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](spl.md)
