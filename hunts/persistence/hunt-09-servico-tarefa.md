# HUNT-WIN-009: Serviço ou tarefa criada

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Revisar configuração persistente e execução posterior quando houver evidência.

Uma tarefa ou serviço novo pode executar atividade fora da finalidade administrativa; a criação isolada não determina intenção.

## ATT&CK quando aplicável

T1543.003 para Windows Service e T1053.005 para Scheduled Task são candidatas contextuais, não rótulos de toda instalação. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Security 4697/4698 e fontes de execução. Campos: ator, host, serviço/binário/conta/start type ou TaskContent com ação, principal e gatilho.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

N05/N06 em WIN-LAB01, janela principal. Sem criação real de serviço/tarefa no laboratório.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar Security-Auditing, IDs 4697/4698, projetar configuração e ator. Depois buscar execução com identificador/contexto específico, não apenas horário.

**Resultado esperado:** N05 configura LabInventory; N06 cria ClockCheck. N07 tem horário e ferramenta parecidos, mas não há identificador de tarefa ou cadeia que prove execução de N06.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Comparar caminho, conta, ação e gatilho com mudança aprovada.
2. Consultar C04, que só apresenta explicações possíveis.
3. Solicitar fonte de execução de tarefa/serviço e vínculo com processo.
4. Buscar outros hosts com a configuração, diferenciando implantação ampla e abuso.

## Explicações alternativas e limitações

Inventário e checagem de relógio são alternativas legítimas. Binário fictício e ausência de hash impedem atribuição por assinatura/reputação.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

Criações observadas, execução vinculada e autorização inconclusivas. Propor melhoria de coleta ou candidata com contexto, sem inferir persistência maliciosa.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
