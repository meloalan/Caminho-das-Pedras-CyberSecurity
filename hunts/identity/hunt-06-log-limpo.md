# HUNT-WIN-006: Limpeza do log de segurança

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Investigar limpeza e seu contexto sem atribuir intenção automaticamente.

Uma limpeza fora do processo esperado pode reduzir evidência e merecer revisão; manutenção autorizada é alternativa.

## ATT&CK quando aplicável

T1070.001 candidata apenas quando houver evidência de finalidade adversária. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

1102 de Microsoft-Windows-Eventlog, canal Security; inventário de manutenção e eventos antes/depois.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

WIN-LAB02, [09:30Z, 10:30Z) de 24/09. Esta janela é diferente da principal para incluir E20 às 10:00.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar provider Eventlog e event_id 1102 no host e intervalo. Não usar provider Security-Auditing para esse ID.

**Resultado esperado:** E20 às 10:00, ator WIN-LAB02/admin.lab. C05 não fornece ticket que confirme manutenção. O fixture não fornece eventos posteriores nessa janela.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Conferir ator, autoridade e hora original.
2. Examinar eventos antes e depois com cobertura/retenção declaradas.
3. Verificar manutenção e logs encaminhados que tenham sobrevivido localmente à limpeza.
4. Expandir para outros hosts sem supor que mesmo nome de conta é a mesma identidade.

## Explicações alternativas e limitações

Manutenção, exercício autorizado ou ocultação. Ausência de eventos depois pode ser limite do fixture ou coleta, não prova de apagamento adicional.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

Limpeza observada; finalidade inconclusiva. Registrar preservação, contexto pendente e revisão de monitoramento, sem executar limpeza real.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
