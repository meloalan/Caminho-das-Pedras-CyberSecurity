# Lab 05: Correlação temporal e casos de borda

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-04-autenticacao.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-processos.md)

## Objetivo

Verificar anterioridade, janela e completude da chave.

## Cenário

Você vai testar a lógica, inclusive exemplos que precisam ser rejeitados.

## Dados

Dataset e cópia de trabalho para simulações. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Qual conjunto precede E04 nos dez minutos anteriores?
2. O que acontece se o sucesso vier antes?
3. E se uma falha empatar com o sucesso?
4. Uma duplicata deve aumentar a quantidade de ocorrências?

## Dicas

Use janela início inclusivo/fim exclusivo para falhas. Não altere o arquivo original.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

Apenas E01/E02/E03 compõem a sequência candidata. Sucesso anterior não satisfaz; falha no mesmo timestamp é rejeitada pela condição estrita. Contar duplicata inflaria o resultado, por isso a identidade do registro precisa ser tratada. Bins fixos não substituem esse teste temporal.

</details>

## Tradução e execução

Use os exemplos completos de [Join não é sinônimo de correlação](../correlacao-e-joins.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

O SPL streamstats ilustrativo exige tratamento de empates; AQL/Query DSL de busca retornam candidatos, não a mesma operação de join KQL.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-04-autenticacao.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-processos.md)
