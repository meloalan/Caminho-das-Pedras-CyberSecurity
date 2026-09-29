# Timeline do incidente

[← Classificação e severidade](classification-and-severity.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Escopo →](scoping.md)

A timeline registra a sequência com fontes e limitações visíveis. Comece cedo e atualize durante o caso. Não transforme proximidade temporal em causalidade. Preserve tanto a hora original quanto a hora normalizada e indique incerteza ou precisão limitada.

## Cinco horários diferentes

| Campo | Significado |
| --- | --- |
| Event time | Quando a fonte diz que a atividade ocorreu. |
| Ingestion time | Quando a plataforma recebeu o registro. |
| Detection time | Quando regra ou pessoa identificou o sinal. |
| Notification time | Quando equipe ou responsável foi informado. |
| Response time | Quando uma ação de resposta começou ou terminou. |

Atraso de ingestão pode fazer um evento antigo parecer recente ou alterar a ordem aparente. Registre a origem do horário, timezone, precisão e qualquer conversão. Use UTC como referência comum quando possível, preservando o valor original. Não converta sem conhecer o fuso e a configuração da fonte.

## Modelo de linha

| Event time UTC | Source | Entity | Event | Confidence | Observação |
| --- | --- | --- | --- | --- | --- |
| 2026-09-29 01:12:00 | IdP LAB | `LAB-EXEC` | Autenticação aceita de `198.51.100.24` | Média | Registro simulado; ingestion 01:19 UTC; fuso do host de origem desconhecido. |
| 2026-09-29 01:16:00 | SIEM LAB | `CASE-101` | Alerta de origem atípica | Alta para hora do alerta | Não confirma comprometimento. |
| 2026-09-29 01:24:00 | Analista LAB | `CASE-101` | Titular contatado por canal alternativo | Média | Ainda sem confirmação. |

Os nomes e registros acima são fictícios. `198.51.100.0/24` é faixa reservada para documentação. Confidence se refere à confiança no evento registrado, não à certeza de que houve comprometimento.

## Boas práticas

- Mantenha identificador de origem ou referência que permita reencontrar o registro.
- Separe evento técnico de decisão, comunicação e ação executada.
- Registre correções com motivo e mantenha auditável o valor original.
- Anote lacunas de cobertura, duplicatas, relógio incorreto e atraso de ingestão.
- Marque claramente observação, inferência e hipótese.

Use timeline junto do [registro do caso](case-management.md), [escopo](scoping.md) e [log de decisão](decision-log.md). O [lab 02](labs/lab-02-timeline.md) pratica normalização sem esconder incerteza.

---

[← Classificação e severidade](classification-and-severity.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Escopo →](scoping.md)
