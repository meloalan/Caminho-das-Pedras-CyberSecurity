# Lab 10: Investigação final multisiem

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-09-detection-query.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../08-Detection-Engineering/README.md)

## Objetivo

Produzir perguntas, queries, pivôs, timeline e conclusão proporcional.

## Cenário

Você recebeu autenticações, privilégios, processo, DNS, rede e criação de conta.

## Dados

Todos os eventos atuais, histórico e inventário. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Quais fatos têm vínculo forte?
2. Qual papel tem E10 como controle?
3. Qual fonte esperada não foi observada?
4. Qual hipótese foi enfraquecida ou permanece aberta?

## Dicas

Separe sessão, processo e criação de conta. Não use apenas proximidade temporal.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

A timeline central é E01/E02/E03 → E04 → E05 → E06 → E07 → E08. A seta organiza tempo e não prova causa. E04/E05/E06 possuem vínculo de sessão no mesmo host; E06/E07/E08 compartilham ProcessGuid. E09 é criação de domínio por admin.lab no DC, sem vínculo demonstrado com a sessão. E10 é homônimo em outra autoridade. WIN-LAB03 está no inventário e não aparece no conjunto. Há lacunas de autorização, comandos posteriores, DNS, hashes e cobertura histórica.

</details>

## Tradução e execução

Use os exemplos completos de [Investigação e timeline: fatos, hipóteses e lacunas](../investigacao.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

Não há conclusão obrigatória de comprometimento. Documente o que cada fonte sustenta e o próximo teste.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-09-detection-query.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../08-Detection-Engineering/README.md)
