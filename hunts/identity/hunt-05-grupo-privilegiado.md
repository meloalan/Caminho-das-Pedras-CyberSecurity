# HUNT-WIN-005: Mudança de grupo e privilégio

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Identificar quem recebeu qual acesso e quem concedeu.

Uma adição a grupo com permissões relevantes pode permitir uso indevido se não for compatível com autorização e finalidade.

## ATT&CK quando aplicável

T1098 é referência candidata de manipulação de conta, condicionada ao contexto adversário. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

4728, 4732 ou 4756 conforme escopo. Campos: member/SID, group/SID, actor, autoridade, host, tempo; inventário de permissões.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

E14/E15/N01 na janela principal. Grupo global de domínio e grupo local não são intercambiáveis.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar Security-Auditing e IDs de adição; manter membro, grupo e ator em colunas distintas. Não buscar 4672 como substituto da concessão.

**Resultado esperado:** E14: novo.lab em Lab-Global-Operators no DC, direitos não fornecidos. E15: local.lab em Administrators do WIN-LAB01. N01: LAB/novo.lab em Administrators do WIN-LAB02.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Conferir SID do grupo e escopo das permissões.
2. Resolver membro com autoridade correta; C03 só se aplica a novo.lab.
3. Buscar autenticação/execução da identidade membro, N02/N03 para novo.lab.
4. Solicitar aprovação e necessidade do acesso; não unir E15 por nome de grupo.

## Explicações alternativas e limitações

Provisionamento e manutenção são alternativas. Nome Operators não demonstra privilégio; 4672 posterior não explica quem concedeu.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

Duas adições locais relevantes observadas; autorização não demonstrada. Encaminhar revisão de acesso e avaliar candidata com escopo correto.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
