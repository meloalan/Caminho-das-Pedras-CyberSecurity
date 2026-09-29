# Papéis e responsabilidades

[← Preparação](preparation.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Detecção e análise →](detection-and-analysis.md)

Os títulos variam entre organizações. O essencial é não deixar sem dono as funções de investigar, decidir, executar, aprovar e informar. Uma pessoa pode acumular papéis em uma equipe pequena, desde que conflito de interesse, carga e autoridade estejam claros.

| Papel ilustrativo | Responsabilidade possível |
| --- | --- |
| Incident Handler | Conduz análise técnica, mantém estado do caso e propõe próximos passos. |
| Incident Commander ou IR Lead | Quando adotado, coordena objetivos, prioridades, decisões, pendências e comunicação. Não precisa executar cada tarefa. |
| SOC Analyst | Valida sinal, enriquece contexto e encaminha achados com fontes. |
| DFIR | Orienta aquisição e análise forense conforme escopo e procedimento aprovado. |
| IAM, rede, endpoint, cloud, infraestrutura, aplicações | Avaliam impacto técnico e executam ações no domínio sob aprovação aplicável. |
| Dono do serviço ou negócio | Avalia criticidade, impacto e opções de continuidade. |
| Jurídico e privacidade | Avaliam questões legais, contratuais, regulatórias e de dados pessoais. |
| Comunicação | Prepara mensagens apropriadas aos públicos e canais. |
| Patrocinador executivo | Resolve prioridade e risco que ultrapassam a autoridade operacional. |

## RACI ilustrativo

R executa, A responde pela decisão final no escopo acordado, C é consultado e I é informado. A matriz abaixo é apenas exemplo: confirme a política local e nomeie pessoas ou cargos reais fora deste exercício.

| Atividade | SOC | IAM | Infra | IR Lead | Dono do negócio |
| --- | --- | --- | --- | --- | --- |
| Investigar autenticação | R | C | I | A | I |
| Recomendar contenção | C | R | C | A | C |
| Aprovar restrição de conta | C | R | I | C | A* |
| Executar restrição aprovada | I | R | I | A | C |
| Restaurar serviço | C | C | R | A | C |

`*` A aprovação pode pertencer a IAM, segurança, negócio ou autoridade delegada, conforme risco e política. A tabela não concede autoridade real.

## Coordenação e comando

Em caso relevante, uma pessoa precisa manter objetivo atual, prioridades, decisões, responsáveis, timeline, pendências e cadência de comunicação. Uma função de coordenação reduz ordens conflitantes e libera especialistas para executar. Incident Commander não é exigência universal. Em equipes pequenas, documente quem está coordenando e quem aprova cada ação.

Uma atualização de coordenação responde: o que sabemos, o que não sabemos, o que mudou desde a última atualização, qual risco é imediato, qual decisão está pendente, quem é responsável e quando reavaliar. Mantenha uma única fonte de estado, com acesso apropriado.

## Exercício

Para o cenário de conta executiva, atribua responsáveis por validar atividade, contatar o usuário por canal confiável, revisar sessões, avaliar impacto de eventual bloqueio, aprovar contenção, preservar registros, comunicar liderança e atualizar o handoff. Se uma função estiver sem responsável, isso é uma lacuna de preparação.

**Entrega:** RACI fictício acompanhado das suposições e dos papéis sem cobertura.

---

[← Preparação](preparation.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Detecção e análise →](detection-and-analysis.md)
