# HUNT-WIN-003: Processo incomum em população conhecida

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Priorizar execuções por contexto e baseline, não pelo nome isolado.

Uma relação parent-child não observada no histórico pode representar nova automação legítima ou uso indevido que merece revisão.

## ATT&CK quando aplicável

T1059.001 é candidata apenas se PowerShell estiver ligado a comportamento adversário; raridade não é técnica ATT&CK. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Sysmon 1 e Security 4688; baseline.csv. Campos: image, parent_image, command_line, user, host, process_guid/PID e tempo.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

WIN-LAB01/02 com cobertura de processos, janela principal; baseline de 17 a 23/09.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar criação de processo por provider e ID, projetar pai, comando e identidade; comparar cada relação com população histórica equivalente.

**Resultado esperado:** N04 registra Office → PowerShell sem ocorrência no baseline fornecido. E12/E13 representam a mesma criação de processo por duas fontes. inventory.exe é raro, mas C06 fornece contexto aprovado para sua ocorrência histórica.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Conferir se a unidade é execução ou registro e não dobrar E12/E13.
2. Priorizar N04 pela combinação pai/usuário e contexto faltante.
3. Solicitar evento do pai, conteúdo do documento e aprovação apropriada; não inventá-los.
4. Expandir para outros hosts apenas com cobertura comparável.

## Explicações alternativas e limitações

Automação de documento, implantação e exercício autorizado podem explicar a relação. O histórico curto não estabelece normalidade universal.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

N04 merece contexto adicional; nenhuma ameaça confirmada. Uma candidata baseada em parent-child exige exemplos legítimos e avaliação de volume.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
