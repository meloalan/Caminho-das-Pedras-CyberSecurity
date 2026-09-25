# Lab 08: Hunting e raridade

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-07-pivot.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-detection-query.md)

## Objetivo

Testar hipótese e registrar contradições.

## Cenário

Você quer investigar relações pai/filho pouco frequentes em ferramentas administrativas.

## Dados

Sysmon 1 de 23 e 24/09/2026; inventário fictício. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Qual relação aparece uma vez?
2. Qual relação foi observada no dia anterior?
3. Dois dias bastam para um baseline?
4. Que evidência sustentaria manutenção legítima?

## Dicas

Não inclua 4688 na contagem de Sysmon. Preserve host na relação.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

PowerShell/explorer em WIN-LAB01 aparece em H01 e E06. PowerShell/taskeng em WIN-LAB02 aparece em E12 uma vez. A segunda relação é rara nesse recorte; a explicação de tarefa administrativa permanece possível. Dois dias e cobertura limitada não sustentam baseline estável. Solicite histórico e contexto da tarefa.

</details>

## Tradução e execução

Use os exemplos completos de [Threat hunting: da hipótese à revisão](../threat-hunting.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

Raridade, novidade e confiança de fonte são dimensões diferentes. Não chame ausência no recorte de nunca ocorrido.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-07-pivot.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-detection-query.md)
