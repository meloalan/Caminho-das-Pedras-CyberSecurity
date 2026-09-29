# ATT&CK em Incident Response

[← Índice do módulo](README.md) · [SOC](attack-for-soc.md) · [Threat Hunting](attack-for-threat-hunting.md) · [Mitigações](mitigations.md)

## Comportamento ajuda a organizar a investigação

Durante resposta a incidente, ATT&CK ajuda a registrar ações observadas e indicar perguntas subsequentes. Não substitui linha temporal, evidência forense, preservação, escopo, análise de impacto nem critérios de contenção.

Para cada comportamento relevante, mantenha:

1. Evidência original, proveniência e horário.
2. Observação literal e contexto do sistema.
3. Técnica candidata, domínio e versão ATT&CK.
4. Justificativa e confiança analítica local.
5. Hipóteses alternativas e dados ausentes.
6. Relação com ativos, identidades e outros eventos do caso.
7. Próxima ação de coleta, contenção, erradicação ou recuperação.

Não use posição de matriz como cronologia. O tempo vem dos dados do incidente; uma técnica pode ocorrer várias vezes, em paralelo ou fora da sequência visual da matriz.

## Atribuição e comunicação

Um relatório pode associar Group, Software ou Campaign a técnicas. Isso ajuda a formular perguntas e comparar comportamento, mas a relação pública não atribui automaticamente a atividade investigada. Preserve cadeias de evidência e separe conclusão analítica de referência ATT&CK.

## Integração com o módulo 10

O módulo 10 define preparação, detecção, análise, contenção, erradicação, recuperação e aprendizado. ATT&CK dá linguagem comum para registrar comportamento durante essas fases e transformar lacunas em melhoria. Não substitui os processos de resposta.
