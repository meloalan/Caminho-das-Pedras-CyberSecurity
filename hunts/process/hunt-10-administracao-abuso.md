# HUNT-WIN-010: Administração legítima ou potencial abuso

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Comparar explicações concorrentes com evidência discriminante.

Execuções similares podem ter finalidades distintas; documentação independente e relações de processo podem enfraquecer ou sustentar suspeitas delimitadas.

## ATT&CK quando aplicável

T1059.001 é referência de possível abuso; não atribuir técnica adversária a N07 aprovado apenas por usar PowerShell. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Eventos E06/E12/N04/N07, baseline e contexto C01/C02/C06; campos de execução, pai, identidade, host e tempo.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

Dois hosts com processo observável, janela principal e histórico de sete dias; sem ampliar autorização por semelhança.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar as execuções candidatas e construir uma matriz por identidade, pai, comando, baseline, rede e evidência administrativa.

**Resultado esperado:** N07 possui C02 específico; E06 possui apenas C01 insuficiente; N04 é relação rara sem aprovação; E12 possui histórico de automação, não prova de autorização atual.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Escrever explicação legítima e indevida para cada execução.
2. Conferir se aprovação corresponde a host, conta, janela e finalidade.
3. Priorizar contexto faltante de N04/E06 sem confirmar ataque.
4. Registrar dado que faria rever cada conclusão; não criar whitelist por prefixo svc_.

## Explicações alternativas e limitações

Conta autorizada pode ser comprometida; histórico pode conter abuso. Ticket falso ou fora de escopo não resolve a hipótese. No cenário C02 é contexto independente explicitamente fornecido.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

N07: hipótese de finalidade indevida enfraquecida no cenário. E06/N04: inconclusivas. E12: contexto de automação, ainda dependente de revisão. Entregar matriz, não um veredito global.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
