# HUNT-WIN-007: Processo e conexão

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Associar comunicação a uma execução real e avaliar explicações concorrentes.

Uma execução pode comunicar-se com destino incompatível com sua finalidade; é preciso contexto para diferenciar aplicação legítima e uso indevido.

## ATT&CK quando aplicável

Sem técnica de C2 atribuída automaticamente: IP/porta e processo não demonstram finalidade ou protocolo de aplicação. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Sysmon 1/3. Campos: host, ProcessGuid, image, user, timestamp, destination_ip/port e protocol.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

WIN-LAB01, janela principal; cobertura de Sysmon 3 declarada no exercício.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar Sysmon 3; buscar Sysmon 1 com mesmo host e ProcessGuid, sem substituir por PID isolado.

**Resultado esperado:** E08 se relaciona a E06. N08/N09/N10 se relacionam a N07. Não há bytes ou conteúdo; intervalos N08→N09 e N09→N10 são 300 segundos.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Recuperar pai/comando da execução correspondente.
2. Comparar identidade, finalidade e destino com contexto independente.
3. Verificar C02 para N07, sem aplicá-lo a E06.
4. Pesquisar outros hosts/destinos mantendo escopo de coleta; WIN-LAB02 não permite o mesmo teste.

## Explicações alternativas e limitações

Monitoramento, atualização e sessões administrativas podem comunicar periodicamente. Três conexões não sustentam uma classificação de beaconing adversário.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

Relações processo/conexão sustentadas; C02 favorece explicação legítima para N07. E06 continua inconclusivo quanto à finalidade.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
