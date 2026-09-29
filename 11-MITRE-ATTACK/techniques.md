# Técnicas

[← Índice do módulo](README.md) · [Subtécnicas](sub-techniques.md) · [Procedures](procedures.md) · [Página principal](../README.md)

## Técnica descreve comportamento

Uma técnica ATT&CK é uma descrição comportamental ampla associada a um objetivo tático. Ela não é um evento, uma ferramenta, um indicador de comprometimento ou uma regra pronta. Um único identificador agrupa manifestações diferentes, em plataformas distintas.

Use [T1136, Create Account](https://attack.mitre.org/techniques/T1136/) como exemplo. O objeto vigente tem subtécnicas para contas locais, de domínio e de nuvem. O mapeamento exige evidência de que uma conta foi criada e contexto suficiente para escolher a forma específica. Uma conta legítima criada por um administrador pode se manifestar de modo parecido; o ID sozinho não decide intenção.

Outro exemplo é [T1059.001, PowerShell](https://attack.mitre.org/techniques/T1059/001/). A técnica descreve uso do interpretador como comportamento. Ela não afirma que toda execução de PowerShell seja maliciosa. O contexto do processo, usuário, host, argumentos disponíveis, origem, horário e atividade relacionada altera a hipótese.

## Técnica não é Event ID

```text
T1136 descreve comportamento
Event ID 4720 registra um evento Windows relacionado à criação de uma conta
```

Não há equivalência `T1136 = 4720`. O evento 4720 pode sustentar uma manifestação de criação de conta Windows. O sistema onde foi gerado, a função do host e o objeto afetado ajudam a determinar se a conta é local ou de domínio. Outros sistemas e provedores de identidade usam outras fontes.

Da mesma forma, Sysmon Event ID 1 é um evento de criação de processo. Sozinho, não prova que o processo executou PowerShell, nem que o uso foi adversário. Verifique imagem, linha de comando se coletada, processo pai, usuário e telemetria complementar. A [documentação Microsoft de eventos Sysmon](https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/sysmon-events) define os eventos e seus dados. A [documentação Microsoft do evento 4720](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4720) explica os contextos Windows nos quais a auditoria pode registrá-lo.

## Leitura de uma técnica

Antes de mapear, registre:

| Pergunta | Aplicação |
| --- | --- |
| Que comportamento foi observado? | Descreva ações e objetos, sem começar pelo ID. |
| Que parte da descrição ATT&CK corresponde? | Compare a evidência com a página vigente e inclua a versão. |
| Qual objetivo tático é plausível? | Trate objetivo como hipótese contextual, não como fato automático. |
| Qual plataforma está em escopo? | Registre onde a técnica é aplicável e onde sua coleta existe. |
| O que contradiz a hipótese? | Procure ações legítimas, explicações alternativas e dados ausentes. |
| Qual precisão é sustentada? | Use a técnica pai quando a evidência não diferencia uma subtécnica. |

Consulte [como ler uma página de técnica](reading-attack-technique.md) para examinar plataformas, relações, detecção e mitigação sem tratar cada campo como prova.

## Exemplo: criação de conta

Observação hipotética: um evento de auditoria registra criação de uma conta `svc-relatorios` em um servidor Windows. Isso sustenta a investigação de criação de conta. Para associar subtécnica e objetivo, o analista ainda precisa confirmar o escopo do objeto, o papel do host, a identidade que executou a ação, o processo associado e se a alteração foi autorizada. Se esses dados não existem, registre a incerteza em vez de promovê-la a conclusão.

## Exercício

Uma regra gera alerta para criação de contas locais em uma imagem específica do Windows, mas não coleta alterações de diretório nem eventos de provedores cloud.

1. Que comportamento e subtécnica estão cobertos pelo escopo da regra?
2. Quais condições e campos a regra exige?
3. Quais ambientes ficam fora do escopo?
4. Que telemetria adicional apoiaria uma investigação?
5. Que formulação descreve o limite sem alegar cobertura completa de T1136?

## Entrega para o portfólio

Registre a observação, o objeto ATT&CK candidato, a evidência que sustenta o mapeamento, hipóteses alternativas, a versão usada e os limites da conclusão. Um mapeamento é auditável quando outra pessoa consegue reproduzir esse raciocínio.
