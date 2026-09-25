# Lab 03: Agregações e denominadores

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-02-filtros.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-autenticacao.md)

## Objetivo

Distinguir evento, grupo, origem distinta e percentual.

## Cenário

Você precisa comparar falhas por host e por identidade sem contar homônimos como a mesma pessoa.

## Dados

Cinco eventos 4625 do dia. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Quantas falhas em cada host?
2. Quantas por domínio+usuário?
3. Qual percentual está em WIN-LAB01?
4. Quantas origens distintas por identidade?

## Dicas

Agrupe manualmente antes de consultar. O denominador é cinco registros de falha, não todos os eventos.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

WIN-LAB01=4 e WIN-LAB02=1. LAB/alan.lab=3, OUTRO/alan.lab=1, LAB/svc.lab=1. WIN-LAB01 representa 80% das falhas observadas. Cada identidade tem uma origem distinta no fixture. O percentual não mede ataques; E10 explica por que agrupar apenas por nome é inadequado.

</details>

## Tradução e execução

Use os exemplos completos de [Agregações: o que exatamente você está contando?](../agregacoes.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

Na plataforma, coalescência, duplicação, campos ausentes e cardinalidade aproximada podem impedir comparação direta.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-02-filtros.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-autenticacao.md)
