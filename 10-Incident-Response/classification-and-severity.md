# Classificação e severidade

[← Detecção e análise](detection-and-analysis.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Timeline →](incident-timeline.md)

Classificação dá linguagem comum para priorizar trabalho. Não é pontuação universal nem substitui julgamento. Use a política da organização, registre a razão e reavalie quando escopo ou impacto mudar. Diferencie severidade técnica do sinal, prioridade operacional e estado formal do caso.

## Dimensões úteis

| Dimensão | Pergunta |
| --- | --- |
| Confiança | Quão confiável e corroborado é o sinal? |
| Atividade | O evento está em curso? Há sessão ou propagação ativa? |
| Impacto | Que serviço, dado, pessoa ou operação pode ser afetado? |
| Exposição | O ativo é acessível externamente ou contém informação sensível? |
| Privilégio | Que alcance teria a identidade ou sistema? |
| Escopo | Quantas entidades estão confirmadas ou possivelmente relacionadas? |
| Continuidade | Que efeito a contenção pode causar em operação, segurança ou recuperação? |
| Obrigações | Há questão contratual, regulatória ou legal a encaminhar? |

Documente os fatos por dimensão e o que falta saber. Confiança baixa não significa automaticamente baixa prioridade: um sinal incerto sobre ativo crítico pode exigir validação urgente. Confiança alta também não implica interrupção imediata se houver alternativa segura, mas a decisão precisa considerar o risco de esperar.

## Exemplo de política local

Os rótulos abaixo são ilustrativos. Adapte nomes, critérios, prazos e aprovações à política real.

| Nível fictício | Exemplo de condição | Resposta esperada |
| --- | --- | --- |
| P1 | Dano ativo plausível em serviço crítico ou identidade privilegiada com atividade corroborada. | Acionar coordenação imediatamente e decidir contenção proporcional com autoridade definida. |
| P2 | Comprometimento provável, escopo limitado ou impacto relevante ainda em validação. | Designar handler, ampliar escopo e estabelecer atualização próxima. |
| P3 | Sinal plausível sem evidência de impacto imediato, com fonte disponível para validação. | Investigar no prazo local e reclassificar diante de novos fatos. |
| Observação | Atividade explicável ou inconclusiva sem critérios locais de incidente. | Registrar resultado e lacuna; não chamar incidente sem base. |

Se o caso muda, registre valor anterior, novo valor, evidência e responsável. Não use um score calculado para autorizar bloqueio automaticamente.

## Classificação não é crise

Um incidente de alta severidade pode exigir coordenação ampliada, mas “crise” costuma depender de impacto organizacional, continuidade, liderança e comunicação. Defina os critérios com a governança local. Se dados pessoais, segurança física ou obrigações contratuais puderem estar envolvidos, escale as áreas competentes sem declarar conclusão legal prematura.

---

[← Detecção e análise](detection-and-analysis.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Timeline →](incident-timeline.md)
