# Lab 07: Pivôs com chaves verificáveis

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-06-processos.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-threat-hunting.md)

## Objetivo

Passar de processo para DNS/rede e reconhecer onde parar.

## Cenário

A pesquisa inicial encontrou E06 e você precisa avaliar observações relacionadas.

## Dados

E06/E07/E08/E09 e seus campos. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Qual campo liga E06 a E07/E08?
2. O DNS resolveu para o IP de E08?
3. Qual evidência ligaria E09 ao processo?

## Dicas

Use host+ProcessGuid e janela. Uma resposta DNS não está no fixture.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

E06/E07/E08 compartilham a execução sintética. O dataset não contém resolução DNS, portanto não prova domínio→IP. E09 tem outro ator e ocorre no DC; o vínculo causal não está demonstrado. A investigação deve parar esse salto ou pedir evidência adicional.

</details>

## Tradução e execução

Use os exemplos completos de [Pivot: transforme um achado em outra pergunta](../pivot.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

A Query DSL precisa de paginação completa; timestamps de processamento podem diferir da ocorrência.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-06-processos.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-threat-hunting.md)
