# Anti-patterns de mapeamento

[← Índice do módulo](README.md) · [Técnicas](techniques.md) · [Cobertura](detection-coverage.md) · [Versionamento](versioning-attack.md)

## Erros que distorcem a análise

| Anti-pattern | Por que falha | Correção |
| --- | --- | --- |
| `T1136 = Event ID 4720` | Um objeto comportamental não é um evento de plataforma. | Descreva fonte, evidência e escopo. |
| `Sysmon 1 = PowerShell` | Evento de processo não prova por si só qual conteúdo foi executado ou a intenção. | Examine imagem, campos coletados, contexto e fontes complementares. |
| Tag de regra = cobertura total | Mapeamento não mede escopo nem eficácia. | Registre manifestações, plataformas, ativos e validação. |
| Técnica como etapa obrigatória | Matriz não define a sequência real de um incidente. | Use horários e evidência para estabelecer cronologia. |
| Todas as técnicas como checklist | Relevância e risco variam entre ambientes. | Priorize por risco, exposição, dados e capacidade de resposta. |
| Ferramenta conhecida = atividade maliciosa | Ferramentas têm usos legítimos e contextos diversos. | Avalie processo, usuário, propósito e atividade associada. |
| Técnica compartilhada = ator atribuído | Relação pública não é prova específica do caso. | Use várias fontes independentes e registre incerteza. |
| Percentual sem denominador | Esconde dados ausentes e diferenças de escopo. | Defina população, método, validade e limitações ou não use percentuais. |
| Data Source antigo como modelo atual | Esse tipo de objeto foi depreciado a partir da v18. | Consulte Detection Strategies, Analytics e Data Components atuais. |
| ID sem versão | Descrição, relações e taxonomia podem mudar. | Registre ID, domínio, versão e data da análise. |

## Teste rápido de uma tag

Antes de publicar uma tag ATT&CK numa detecção, pergunte:

1. Que frase concreta explica a relação da regra com o comportamento?
2. A lógica observaria alguma atividade legítima igual?
3. Que manifestações ficam fora da regra?
4. Que evidência de teste valida o mapeamento?
5. O mapeamento aponta domínio e versão?

Se as respostas faltam, ajuste o rótulo ou deixe o mapping como hipótese.
