# ATT&CK no SOC

[← Índice do módulo](README.md) · [Threat Hunting](attack-for-threat-hunting.md) · [Incident Response](attack-for-incident-response.md)

## Uma linguagem de triagem

No SOC, ATT&CK ajuda a descrever comportamento, tornar alertas comparáveis e levantar perguntas de investigação. Ele não substitui evidência do alerta nem determina prioridade sozinho.

Ao receber um alerta com tag ATT&CK:

1. Examine o evento original e os campos que acionaram a regra.
2. Confirme o comportamento antes de confirmar o mapeamento.
3. Determine ativo, identidade, processo, horário e atividade relacionada.
4. Considere uso legítimo e hipóteses alternativas.
5. Use ATT&CK para orientar pivôs investigativos relevantes.
6. Registre fatos, inferências e lacunas separadamente.
7. Encaminhe gaps de fonte ou lógica ao time responsável.

## Evite atalhos de atribuição

Técnica ou ferramenta associada a um Group não atribui o incidente a esse Group. Atribuição exige contexto e evidências independentes. A presença de uma ferramenta administrativa ou de PowerShell também não torna automaticamente a atividade maliciosa.

## Integração com o módulo 05

O módulo de SOC e Blue Team fornece responsabilidades e fluxo operacional. ATT&CK acrescenta vocabulário para narrar o comportamento e encontrar lacunas. O alerta continua dependendo dos procedimentos de triagem e escalonamento definidos pela organização.

## Nota de caso

Ao fechar um alerta, descreva o que foi visto, qual mapeamento se sustenta, versão consultada, telemetria faltante e se uma hipótese de hunting ou ajuste de regra é recomendada. Não feche a investigação apenas porque um ID foi encontrado.
