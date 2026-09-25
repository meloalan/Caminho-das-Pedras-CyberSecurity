# Lab 02: Filtros e precedência

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-01-entendendo-campos.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-agregacoes.md)

## Objetivo

Construir uma população correta sem perder dados silenciosamente.

## Cenário

Uma consulta deveria manter falhas ou sucessos de WIN-LAB01, mas trouxe outro host.

## Dados

Dataset completo, apenas 24/09/2026. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Qual predicado precisa de parênteses?
2. Quais IDs satisfazem host e EventID?
3. O filtro de origem preenchida serve para 4720?

## Dicas

Escreva (4625 OU 4624) E host. Confira E11 como caso negativo e E09 como exemplo sem IP.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

A população de autenticação de WIN-LAB01 contém E01/E02/E03/E04/E10. E10 permanece porque este exercício ainda não restringe autoridade. E11 fica fora pelo host. Ao investigar LAB/alan.lab, acrescente domínio e exclua E10. Exigir SourceIP para toda consulta ocultaria E09, que não fornece esse dado.

</details>

## Tradução e execução

Use os exemplos completos de [Operadores e transformações: preserve o significado](../operadores-e-transformacoes.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

Aliases e campos dependem do parser. Null, vazio e hífen precisam de tratamento explícito em cada produto.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-01-entendendo-campos.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-agregacoes.md)
