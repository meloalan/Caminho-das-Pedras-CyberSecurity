# AQL: perguntar ao Ariel sem presumir SQL genérico

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](spl.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](wazuh-opensearch.md)

## Dataset, propriedade e unidade

Ariel Query Language consulta os dados do Ariel. `events` contém registros de eventos; `flows` contém registros de fluxos com campos próprios. Eles não são tabelas intercambiáveis. Um flow não é captura integral de pacotes; uma comunicação longa pode gerar vários registros.

O contrato deste módulo usa propriedades customizadas `Lab*`, extraídas/validadas no DSM Editor. `LabEventID` é texto. QID identifica a categoria do QRadar e não deve receber 4625 como se fosse Windows Event ID. AQL faz pesquisa; CRE aplica regras operacionais com estado e respostas.

## Estrutura e ordem das cláusulas

| Cláusula/recurso | Papel |
| --- | --- |
| SELECT | Propriedades e expressões de saída |
| FROM | events ou flows conforme pergunta |
| WHERE | Filtro antes do agrupamento |
| GROUP BY | Dimensões do grupo, presentes no SELECT |
| HAVING | Condição sobre agregado |
| ORDER BY | Ordem da saída |
| LIMIT | Máximo de linhas retornadas |
| LAST ou START/STOP | Janela no final da instrução |
| AS | Alias, sem criar uma propriedade persistente |
| COUNT(*) | Linhas armazenadas |
| SUM(eventcount) | Ocorrências representadas quando há coalescência |
| UNIQUECOUNT | Valores distintos da propriedade |

Não transporte `COUNT(DISTINCT ...)` ou `SELECT DISTINCT` de outro dialeto sem confirmar suporte da versão. Aqui usamos UNIQUECOUNT para contar valores distintos e GROUP BY para listar combinações. Não ter TIMEFRAME pode aplicar uma janela padrão inesperada; sempre declare tempo.

```sql
SELECT "LabDomain", "LabUser", SUM(eventcount) AS falhas, UNIQUECOUNT("LabSourceIP") AS origens
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing' AND "LabEventID" = '4625'
GROUP BY "LabDomain", "LabUser"
HAVING SUM(eventcount) >= 3
ORDER BY falhas DESC
LIMIT 20
LAST 24 HOURS
```

SELECT define dimensões e métricas; WHERE delimita falhas; GROUP BY mantém autoridade e conta separadas; HAVING testa agregado; ORDER BY/LIMIT controla exibição; LAST fixa a janela relativa. Limite três é didático. Campos ausentes, coalescência e origem compartilhada alteram a interpretação.

## Events versus flows na prática

```sql
SELECT sourceip, destinationip, SUM(sourceBytes) AS bytes_origem
FROM flows
GROUP BY sourceip, destinationip
ORDER BY bytes_origem DESC
LIMIT 10
LAST 1 HOURS
```

Essa consulta responde quais pares acumulam mais bytes de origem observados, não quais IPs estão atacando. `sourceBytes` pertence ao contrato de flows, não ao XML Windows. O dataset dos labs não contém flows e não fornece resultado esperado para esse exemplo operacional.

## Tempo, strings e contexto

DATEFORMAT ajuda a agrupar/mostrar horários, mas conferir fuso continua obrigatório. LOWER, ILIKE e IMATCHES têm usos diferentes. Reference maps/tables acrescentam contexto quando previamente criados; não substituem um join temporal arbitrário. [Tempo](tempo-em-queries.md), [strings](strings-e-regex.md) e [lookups](lookups-e-enriquecimento.md) desenvolvem essas decisões.

## Fontes oficiais e teste

[Estrutura AQL](https://www.ibm.com/docs/en/qsip/7.5.0?topic=structure-sample-aql-queries), [agregações](https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-aql-data-aggregation-functions) e [funções de cálculo](https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-aql-data-calculation-formatting-functions) sustentam os exemplos. Documentação 7.5 é a base explícita; confirme compatibilidade na instalação 7.6 ou posterior. Revisão documental não equivale a execução no Console.

Prática: compare COUNT(*) com SUM(eventcount) numa amostra coalescida e explique a diferença. Sem QRadar, represente duas linhas de pesos 1 e 4: são duas linhas e cinco ocorrências, não cinco registros independentes disponíveis para sequência.

## Checkpoint

**Uma query AQL agregada cria uma offense?**

<details>
<summary>Ver resposta</summary>

Não. A pesquisa produz resultados. CRE, respostas e critérios de offense são configuração operacional distinta.

</details>

[← Tópico anterior](spl.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](wazuh-opensearch.md)
