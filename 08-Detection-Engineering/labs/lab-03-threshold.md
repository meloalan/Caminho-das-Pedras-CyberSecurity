# Lab 03: Threshold: 3, 5 ou 10?

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-02-primeira-deteccao.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-correlacao-temporal.md)

## Objetivo

Medir mudanças de alcance ao alterar limiar.

## Cenário

O fixture compartilhado tem três falhas válidas antes de um sucesso. Há controles com outra autoridade e outro host.

## Dados e preparação

Use os 22 eventos fictícios do módulo 07; o avaliador local pode repetir o cálculo.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Quantas sequências aparecem com 3, 5 e 10?
2. Por que não contar E10 junto de E01/E02/E03?
3. O que o limiar maior perde?
4. Que cenário N-1/N/N+1 falta testar?

## Dicas

Conte ocorrências únicas da mesma chave dentro dos dez minutos anteriores. Não conte volume global por dia.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

As saídas são 1, 0 e 0. E10 pertence a OUTRO, não LAB. E11 pertence a outro host/conta. O limiar maior perde a sequência do exercício; isso não demonstra que três seja o melhor valor em produção. Acrescente cenários artificiais com 4/5/6 e 9/10/11 ocorrências e documente a diferença entre contagem e intenção.

</details>

## Implementação e limites

Use [Testes reproduzíveis com dados fictícios](../testing-detections.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Tabela de limiares, população, perdas e decisão justificada. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Quantas sequências aparecem com 3, 5 e 10?**

<details>
<summary>Ver resposta</summary>

As saídas são 1, 0 e 0.

</details>

[← Tópico anterior](lab-02-primeira-deteccao.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-correlacao-temporal.md)
