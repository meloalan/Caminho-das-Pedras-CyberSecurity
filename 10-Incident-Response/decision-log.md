# Registro de decisões

[← Escopo](scoping.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Contenção →](containment.md)

O log de decisões mostra por que a equipe escolheu agir, esperar ou mudar de rumo. Ele reduz repetição, apoia handoff e permite revisão. Registre a decisão no momento; não reconstrua justificativa depois como se fosse contemporânea.

## Estrutura mínima

| Campo | Pergunta |
| --- | --- |
| Hora e responsável | Quando foi decidido e quem coordenou? |
| Situação | Qual pergunta precisava de resposta? |
| Evidências | Quais fatos e fontes sustentam a decisão? |
| Incerteza | O que é inferência ou ainda desconhecido? |
| Opções | Que alternativas foram consideradas, inclusive não agir? |
| Impacto | Que risco técnico, operacional, humano ou de dados existe? |
| Autoridade | Quem recomendou, aprovou e executará? |
| Escolha | O que foi autorizado, com que escopo e limites? |
| Reversão | Como e por quem pode ser revertida? |
| Revisão | Qual condição, responsável e horário reabrem a decisão? |

## Exemplo fictício

| Campo | Registro |
| --- | --- |
| Hora UTC | 2026-09-29 01:35 |
| Situação | Origem atípica para `LAB-EXEC`; titular ainda não validado. |
| Fatos | IdP registra autenticação aceita. Atividade em duas aplicações ainda em análise. |
| Desconhecidos | Sessões ativas, legitimidade, uso de dados e escopo de outras contas. |
| Opções | Suspender identidade; revogar sessão observada; restringir temporariamente; validar em paralelo. |
| Escolha | Exercício autoriza revogar apenas a sessão simulada e confirmar por fonte independente. |
| Razão | Reduz acesso observado com impacto menor que suspender toda a identidade. |
| Aprovação/execução | Papéis fictícios IR Lead / IAM LAB. Não é autorização real. |
| Reavaliação | Ao confirmar titular, identificar nova sessão ou após 15 minutos do exercício. |

O intervalo é apenas parte deste cenário didático, não recomendação de prazo. Registre quando a execução difere do autorizado e por quê.

**Use:** [modelo copiável de decisão](TEMPLATE-DECISION-LOG.md) e [lab 04](labs/lab-04-containment-decisions.md).

---

[← Escopo](scoping.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Contenção →](containment.md)
