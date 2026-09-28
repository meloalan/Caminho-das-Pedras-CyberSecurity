# Hipóteses testáveis e concorrentes

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](metodologia.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](bias-e-raciocinio.md)

## Especificidade sem antecipar a conclusão

“Existe malware na empresa” não define observáveis nem limites. Uma hipótese útil é específica, observável, testável, limitada, comportamental e capaz de ser enfraquecida ou refutada.

> Se uma identidade estiver sendo usada indevidamente para administrar endpoints Windows, podemos observar autenticações e execuções de PowerShell incompatíveis com sua função, origem habitual e mudanças autorizadas no grupo observado.

Essa hipótese não afirma que PowerShell é ataque. Também não exige PowerShell como único meio de administração. O hunt investiga uma manifestação delimitada; outros meios continuam fora do seu alcance.

| Elemento | Decisão de exemplo |
| --- | --- |
| Identidade e população | LAB/alan.lab em WIN-LAB01; expandir só com justificativa |
| Período | 24/09/2026, 08:00 a 10:00 UTC, fim exclusivo |
| Observáveis | Conta, origem, logon type, sessão, processo pai, comando e conexões |
| Sustentaria | Relação de sessão e atividade incompatível corroborada por contexto independente |
| Enfraqueceria | Mudança aprovada coerente, responsável e finalidade confirmados |
| Refutaria | Evidência suficiente contradiz a proposição específica testada |
| Inconclusivo | Falta de command line, autorização ou cobertura necessária |

## Hipótese não é conclusão

A hipótese propõe uma explicação. A conclusão compara evidências disponíveis com essa explicação. “O atacante executou PowerShell” presume identidade adversária que um evento de processo não demonstra.

## Hipóteses concorrentes

| Explicação | Dados que ajudam a diferenciá-la |
| --- | --- |
| Uso indevido de credenciais | Origem, contexto de sessão, aprovação independente e ações posteriores |
| Administração legítima | Ticket, janela, escopo, operador e tarefa executada |
| Software corporativo | Processo pai, assinatura, distribuição e documentação do produto |
| Automação | Agendamento, conta de serviço, periodicidade e configuração |

Não basta encontrar um ticket com horário parecido. Compare identidade, host, tarefa e aprovação; uma conta autorizada também pode ser comprometida.

## Antes de executar

Escreva o que espera encontrar, o que espera não encontrar e o que enfraqueceria a hipótese. Declare se a proposição é sobre existência de uma sequência ou sobre intenção indevida. Os dados podem sustentar a sequência e deixar sua intenção inconclusiva.

Prática: reescreva “PowerShell suspeito” com escopo e duas alternativas. Depois execute o [Lab 01](labs/lab-01-escrevendo-hipoteses.md).

## Checkpoint

**Zero eventos refuta uma hipótese de abuso?**

<details>
<summary>Ver resposta</summary>

Só pode contrariar uma previsão específica quando a cobertura e a capacidade da pesquisa forem suficientes. Caso contrário, a hipótese permanece inconclusiva.

</details>

[← Tópico anterior](metodologia.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](bias-e-raciocinio.md)
