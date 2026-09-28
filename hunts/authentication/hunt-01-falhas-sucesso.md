# HUNT-WIN-001: Falhas seguidas de sucesso

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Investigar se a sequência de autenticação justifica revisão de uso indevido de identidade.

Se uma conta estiver sendo utilizada fora do contexto esperado, falhas e sucesso podem ser acompanhados de origem ou atividade posterior incompatíveis. A sequência sozinha não decide a causa.

## ATT&CK quando aplicável

T1078 é uma referência candidata somente se o uso indevido de conta válida for sustentado; falhas não comprovam brute force ou password spray. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Security 4625/4624, depois 4672 e Sysmon 1. Campos: domínio, user/SID, host, source_ip, logon_type, timestamp, logon_id e process_guid.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

WIN-LAB01, LAB/alan.lab, [08:00Z, 10:00Z) em 24/09/2026. Exigir falhas em [sucesso-10m, sucesso).

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar provider Security-Auditing, event_id em 4624/4625, host WIN-LAB01 e janela. Manter domínio na saída. As quatro consultas de entrada estão no multisiem.

**Resultado esperado:** E01/E02/E03/E04/E10. E10 pertence a OUTRO e não compõe a sequência de LAB. Três falhas antecedem E04 com chave completa.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Separar autoridade/conta antes de contar; E10 é controle negativo.
2. Comparar origem e tipo de logon de falhas e sucesso.
3. Buscar sessão 0xA100 no mesmo host: E05 e E06.
4. Pivotar ProcessGuid: E07/E08. Solicitar autorização e contexto, ausentes para E06.

## Explicações alternativas e limitações

Erro de digitação, senha antiga, administração ou uso indevido. C01 não fornece aprovação suficiente. MFA e VPN não estão no dataset.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

A sequência está observada; abuso inconclusivo. Propor candidata testável com controles de homônimo, janela e nulos; não criar bloqueio automático.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
