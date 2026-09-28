# Métricas com população e denominador

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](detection-health.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](runbooks.md)

## O que medir e por quê

| Métrica | Definição necessária | Cuidado |
| --- | --- | --- |
| Volume de alertas | Contagem de unidades após agrupamento no período | Mudança de agrupamento altera comparação |
| Taxa de alertas | Alertas por hora/dia ou por população declarada | Períodos e ativos diferentes não são comparáveis |
| Investigação iniciada | Casos iniciados / alertas elegíveis | Não mede todos os casos realmente relevantes |
| Classificação | Categorias e evidência após triagem | Inconclusivo não deve virar benigno por conveniência |
| Regras ativas/silenciosas | Regras que dispararam / regras habilitadas no período | Silêncio pode ser esperado ou defeito |
| Saúde de fonte | Fontes observadas / fontes esperadas no inventário | Exige inventário confiável |
| Latência | Distribuição de duração e atraso por fonte | Média pode esconder cauda longa |
| Tempo para tuning | Intervalo entre problema registrado e mudança validada | Velocidade sem regressão aumenta risco |
| Aging | Tempo desde a última revisão válida | Idade isolada não determina inutilidade |

## Precision, recall e FPR

Para uma população com referência conhecida:

```text
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
False Positive Rate = FP / (FP + TN)
Fração de alertas falsos = FP / (TP + FP)
```

Denominador zero torna a métrica indefinida, não automaticamente zero. FPR não é a fração de alertas que a fila classificou como falsos. Em produção, raramente conhecemos todos os negativos e todos os positivos; não prometa recall real sem ground truth adequado. Se a amostra só inclui atividades observáveis, declare essa restrição.

## O tuning visto pelas métricas

No fixture de cem candidatos, 30 são positivos e 70 negativos quanto à necessidade de investigação. A baseline tem precision 30/100 = 30%, recall 30/30 = 100% e FPR 70/70 = 100%. A exclusão ampla tem precision 20/30 ≈ 66,7%, recall 20/30 ≈ 66,7% e FPR 10/70 ≈ 14,3%. A restrita tem precision 30/40 = 75%, recall 30/30 = 100% e FPR 10/70 ≈ 14,3%.

O recall de 100% descreve apenas esses rótulos artificiais. Não avalia comportamentos ausentes do fixture. Os dois tunings têm o mesmo FPR, mas perdas positivas diferentes. Essa comparação mostra por que “menos alertas” não é critério suficiente.

## Unidade antes da conta

Evento, correspondência, alerta agrupado, caso e incidente são unidades diferentes. Uma regra pode produzir cem matches e um alerta agrupado; dividir classificações de casos pelo total de eventos cria uma taxa sem sentido operacional. Documente a transformação e mantenha a mesma unidade no numerador e denominador.

**Entrega:** relatório com população, janela, unidade, rótulos, inconclusivos, métricas, incerteza e decisão. Meça também custo de investigação e efeito na cobertura, sem criar uma meta cega de queda de volume.

## Checkpoint

**20 alertas relevantes entre 30 alertas calculam FPR?**

<details>
<summary>Ver resposta</summary>

Não. Calculam precision 20/30. FPR precisa de todos os negativos conhecidos: FP/(FP+TN).

</details>

[← Tópico anterior](detection-health.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](runbooks.md)
