# HUNT-WIN-008: DNS e processo

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Transformar um match de domínio em investigação comportamental.

Uma consulta a domínio de interesse pode estar ligada a processo cuja finalidade precisa de revisão; match não prova comprometimento.

## ATT&CK quando aplicável

Não mapear DNS isolado para técnica de C2. Mapear somente comportamento demonstrado por evidência adicional. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Sysmon 22/1 e, para aprofundar, DNS com resposta e rede. Campos: query_name, host, process_guid, tempo, usuário e contexto.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

updates.example.test no WIN-LAB01, janela principal; indicador IOC-LAB-001 válido para o cenário, confiança baixa.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar Sysmon 22 com query_name exato; depois buscar execução pelo GUID e host. Não presumir que nome de domínio apareça em toda conexão.

**Resultado esperado:** E07 corresponde ao indicador fictício e leva a E06. E08 está na mesma execução, mas o dataset não fornece resposta DNS para ligá-lo ao domínio.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Registrar validade e origem do indicador, sem consulta a reputação real.
2. Buscar pai, usuário e comando em E06.
3. Procurar resposta DNS ou proxy; se ausente, registrar telemetry gap.
4. Expandir domínio para outros hosts e declarar denominador observável.

## Explicações alternativas e limitações

Atualização, teste ou software corporativo podem explicar o nome. O fixture não contém reputação adversária nem payload.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

Match e relação com processo observados; comprometimento não confirmado. Documentar IOC to Behavior e contexto faltante.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
