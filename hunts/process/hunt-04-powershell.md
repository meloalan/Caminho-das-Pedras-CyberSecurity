# HUNT-WIN-004: PowerShell com contexto de execução

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Investigar finalidade e relações de execuções PowerShell.

Execuções incompatíveis com função, origem ou mudança autorizada podem indicar abuso; ferramentas administrativas esperadas são explicações concorrentes.

## ATT&CK quando aplicável

T1059.001 como referência de comportamento, não classificação automática de toda execução. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Sysmon 1/3/22, Security e contexto. Campos: pai, comando, conta, sessão, GUID, host, destino e horário.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

PowerShell observado no conjunto combinado em 24/09, janela principal, sem executar comandos em endpoints.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar eventos de criação com basename powershell.exe ou pwsh.exe, sem usar contains genérico como conclusão. Conferir o caminho completo e o papel do campo.

**Resultado esperado:** E06, E12, N04 e N07 são criações Sysmon PowerShell. E13 é outra fonte de E12, não nova execução. Só E06 tem DNS no fixture; N07 tem contexto C02 e três conexões.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Comparar E06 explorer, E12 taskeng, N04 WINWORD e N07 taskeng.
2. Consultar a identidade e a sessão quando presentes; N04 não tem logon_id fornecido.
3. Associar rede pelo GUID, mantendo WIN-LAB02 sem cobertura de 3/22.
4. Contrastar autorização específica C02 com ausência de autorização para E06/N04.

## Explicações alternativas e limitações

Administração, automação corporativa e uso indevido continuam hipóteses. -NoProfile não define malícia; Get-Date não prova que nada mais ocorreu numa sessão interativa.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

Separar cada execução e sua confiança. N07 tem explicação legítima corroborada no cenário; E06/N04 seguem dependentes de contexto. Não criar exclusão de todo PowerShell.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
