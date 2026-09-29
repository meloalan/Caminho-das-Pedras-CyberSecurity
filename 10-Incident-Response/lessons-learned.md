# Lessons learned: melhoria contínua

[← Métricas](incident-metrics.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Tabletop →](tabletop-exercises.md)

Uma revisão pós-incidente busca entender o que ocorreu, como decisões e controles funcionaram e que mudanças reduzem risco futuro. O foco é aprendizagem e correção do sistema, sem impedir a apuração apropriada de responsabilidade quando necessária. Faça revisão proporcional ao caso e convide as funções que participaram.

## Perguntas de revisão

- O que esperávamos, e o que aconteceu segundo a evidência?
- Quais sinais ajudaram? Quais faltaram ou chegaram tarde?
- Onde fatos, inferências e desconhecidos foram bem separados?
- A decisão de contenção foi proporcional e autorizada? O que aprendemos sobre impacto e reversão?
- Escopo, coleta e recuperação foram suficientes? Que limitações permanecem?
- Handoff, comunicação e coordenação permitiram agir sem duplicar trabalho?
- Que controle funcionou, que lacuna contribuiu e que evidência sustenta essa conclusão?
- Como testaremos se a melhoria funcionou?

## Ação concreta

Toda melhoria precisa de descrição observável, responsável por papel, prazo aprovado, dependência, critério de conclusão, evidência e teste de eficácia. “Treinar equipe”, “melhorar monitoramento” e “atualizar processo” não são tarefas completas sem público, conteúdo, dono e validação.

| Observação | Melhoria | Dono | Prazo | Teste de eficácia |
| --- | --- | --- | --- | --- |
| O turno seguinte não sabia quem aprovava revogação de sessão. | Atualizar matriz de autoridade e exercitar handoff. | Owner de IAM e IR | Prazo local | No próximo tabletop, participantes encontram aprovador e registram decisão corretamente. |
| Logs de sessão não estavam no caso. | Adicionar fonte e janela ao checklist de triagem. | SOC lead | Prazo local | Exercício demonstra busca reproduzível e documentada. |

Exemplos fictícios. Um item só fecha quando a evidência do teste for revisada, não apenas quando uma alteração for publicada. Categorize melhorias para preparação, detecção, resposta, recuperação ou governança conforme o modelo organizacional. A melhoria é contínua, não uma etapa final exclusiva.

**Entregas:** [template de lessons learned](TEMPLATE-LESSONS-LEARNED.md), relatório pós-incidente, ações com dono e teste; [lab 10](labs/lab-10-lessons-learned.md).

Os [fluxos entre Incident Response, Detection Engineering e Threat Hunting](feedback-loops.md) mostram como transferir achados sem confundir os objetivos das equipes.

---

[← Métricas](incident-metrics.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Tabletop →](tabletop-exercises.md)
