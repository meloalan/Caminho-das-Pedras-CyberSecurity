# Lab 06: Tuning: 100 para 30

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-05-process-creation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-false-negatives.md)

## Objetivo

Comparar volume e perda de casos relevantes.

## Cenário

Uma exclusão por prefixo svc_ promete reduzir a fila.

## Dados e preparação

Use os cem candidatos fictícios em detections/tests/tuning.jsonl e execute evaluate.py.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Quantos TP, FP e FN cada variante produz?
2. Qual ganho é apenas aparente?
3. Qual contexto sustenta a exceção restrita?
4. Que risco permanece dentro da mudança aprovada?

## Dicas

O rótulo requires_investigation serve de referência, não de filtro do detector.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

Baseline: 100 alertas, 30 TP, 70 FP. Exclusão ampla: 30 alertas, 20 TP, 10 FP e 10 FN. Restrita: 40 alertas, 30 TP e 10 FP, sem FN neste fixture. A restrita exige ator/host/janela e registro de aprovação compatíveis. Uma atividade indevida que imite todo o escopo ainda pode escapar: proponha teste e revisão.

</details>

## Implementação e limites

Use [Tuning: reduzir custo preservando o que importa](../tuning.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Relatório de tuning com diff, métricas, risco e rollback. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Quantos TP, FP e FN cada variante produz?**

<details>
<summary>Ver resposta</summary>

Baseline: 100 alertas, 30 TP, 70 FP.

</details>

[← Tópico anterior](lab-05-process-creation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-false-negatives.md)
