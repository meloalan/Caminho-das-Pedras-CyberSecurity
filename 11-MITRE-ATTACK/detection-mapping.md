# Mapeamento de detecções

[← Índice do módulo](README.md) · [Telemetria](attack-to-telemetry.md) · [Detection Strategies](detection-strategies.md) · [Cobertura](detection-coverage.md) · [Página principal](../README.md)

## Mapeie a regra, não o desejo

Uma tag ATT&CK numa regra registra uma relação proposta entre a lógica e um comportamento. Ela não é uma medida de cobertura. Antes de atribuir o ID, pergunte o que a regra realmente detecta, que dados exige, em quais plataformas funciona, como foi testada e quais manifestações não observa.

## Exemplo de mapeamento auditável

| Campo | Exemplo didático |
| --- | --- |
| Regra | Criação de conta local por processo incomum |
| Comportamento alegado | Criação de uma conta local no Windows |
| ID candidato | T1136.001, a confirmar pela evidência do objeto local |
| Tática associada | Persistence, quando esse objetivo é sustentado pelo contexto |
| Fonte e componente | Auditoria de criação de usuário, Data Component DC0014 |
| Telemetria complementar | Criação de processo, DC0032, se coletada e relevante |
| Campos necessários | Host e papel, identificador do alvo, autor, horário, resultado e contexto disponível |
| Limite | Não cobre automaticamente contas de domínio ou cloud, nem toda forma de criação local |
| Estado de validação | Ilustrativo. Só promover a validado após teste reproduzível no ambiente |

Os nomes oficiais de Data Components são [DC0014 User Account Creation](https://attack.mitre.org/datacomponents/DC0014/) e [DC0032 Process Creation](https://attack.mitre.org/datacomponents/DC0032/). Componentes indicam informação de interesse para detecção; não garantem que sua organização coleta essa informação.

## Processo

1. Descreva o comportamento e os fatos observados sem começar pelo identificador.
2. Consulte a técnica e suas subtécnicas na versão registrada em `attack-version.json`.
3. Escolha o mapeamento mais específico que a evidência suporta.
4. Identifique a Detection Strategy relevante, se houver, e os Analytics que podem implementá-la.
5. Ligue cada condição da lógica a uma fonte, um campo e um requisito de coleta.
6. Teste casos positivos e negativos, registre ambiente e resultado.
7. Declare escopo, exceções, dependências, lacunas e data de revisão.
8. Reavalie quando a regra, telemetria, ambiente ou versão ATT&CK mudar.

## Exemplo PowerShell

Uma regra que alerta somente quando `powershell.exe` inicia com uma condição específica observa uma manifestação estreita associada a [T1059.001 PowerShell](https://attack.mitre.org/techniques/T1059/001/). Ela pode deixar de observar execução por outros hosts, argumentos ausentes ou truncados, sessões remotas, diferenças de plataforma e comportamentos fora da condição. A tag descreve a intenção do mapeamento. Para chamar isso de cobertura validada, demonstre o comportamento, a telemetria, a distribuição da coleta, a lógica, os testes e as limitações.

Sysmon Event ID 1 pode fornecer dados de criação de processo, mas não é sinônimo de T1059.001. Verifique configuração, campos coletados e outras fontes necessárias. A [documentação oficial de Sysmon](https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/sysmon-events) descreve o evento e seu conteúdo.

## Integração com os módulos anteriores

- [Módulo 08, Detection Engineering](../08-Detection-Engineering/README.md): a engenharia define hipótese, lógica, validação e ciclo de melhoria. Esta página adiciona uma linguagem de comportamento e um registro de mapeamento explícito.
- [Módulo 09, Threat Hunting](../09-Threat-Hunting/README.md): uma hipótese de hunting conduz à evidência e pode revelar lacuna de telemetria. O hunting não deve começar e terminar numa célula da matriz.
- [Módulo 10, Incident Response](../10-Incident-Response/README.md): o contexto de incidente ajuda a interpretar intenção, relações e impacto. Um alerta mapeado não atribui um grupo adversário.

## Modelo completo

Use [TEMPLATE-ATTACK-MAPPING.md](TEMPLATE-ATTACK-MAPPING.md) para registrar o raciocínio. Use [TEMPLATE-COVERAGE-ASSESSMENT.md](TEMPLATE-COVERAGE-ASSESSMENT.md) quando o objetivo for medir a capacidade defensiva, pois mapeamento e cobertura são perguntas relacionadas, mas diferentes.
