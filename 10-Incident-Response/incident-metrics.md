# Métricas de Incident Response

[← Automação](automation-in-ir.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Lições aprendidas →](lessons-learned.md)

Métricas ajudam a entender capacidade e orientar investimento. Uma única métrica pode incentivar comportamento ruim. Use definições consistentes, contexto, amostras e revisão qualitativa. Não avalie pessoas por “fechar rápido” ou por ausência de incidente reportado.

## Exemplos de indicadores

| Medida | Pergunta | Cuidado |
| --- | --- | --- |
| Tempo até triagem | Quanto demora até alguém avaliar sinal? | Defina início, fim, horário comercial e qualidade da amostra. |
| Tempo até contenção | Quanto tempo até risco relevante ser limitado? | A ação apropriada pode exigir análise e aprovação, não otimize rapidez isolada. |
| Completude do handoff | O turno seguinte recebeu fatos, risco e próximo passo? | Revise amostras, não só presença de campos. |
| Cobertura de timeline | Eventos críticos têm fonte e hora normalizada? | Cobertura depende da telemetria e da qualidade dos relógios. |
| Teste de recuperação | Backups foram restaurados com validação? | “Backup existe” não é indicador suficiente. |
| Ações de melhoria no prazo | Lacunas têm dono e foram fechadas? | Fechamento deve incluir evidência do teste de eficácia. |
| Reabertura ou recorrência | A hipótese voltou a aparecer após retorno? | Investigue cobertura, mudança do ambiente e causa. |

Defina numerador, denominador, exclusões e fonte. Compare tendências dentro de contextos semelhantes. Indicadores não provam causalidade.

---

[← Automação](automation-in-ir.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Lições aprendidas →](lessons-learned.md)
