# Regras Sigma

[← Voltar para página principal](../../README.md)

[Criação de conta Windows](windows-account-created.yml) seleciona 4720 no canal Security. É uma baseline experimental de triagem, não uma prova de persistência.

EventID seleciona o evento; `condition: selection` faz a seleção disparar; `level: low` representa a baixa confiança contextual deste exemplo. Provisionamento autorizado é esperado. Melhore correlacionando responsável, janela de mudança e grupos privilegiados.

A regra genérica usa T1136. No [Lab 02](../../12-Labs-Praticos/02-EventID-4720/README.md), a conta é explicitamente local e permite T1136.001. Não aplique a subtécnica local a todo evento 4720.

Antes de implantar, converta com um pipeline Sigma adequado ao backend e valide os campos com eventos positivos e negativos. Conversão e teste no SIEM ainda estão pendentes. [Formato oficial Sigma](https://sigmahq.io/docs/basics/rules.html).
