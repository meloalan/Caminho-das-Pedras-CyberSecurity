# Versão, owner e histórico de mudança

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](feedback-to-detections.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](retiring-detections.md)

## Identidade estável

DET-WIN-ACCOUNT-001 identifica o caso mesmo quando o título melhora. Use nome que comunique comportamento, como “Windows: criação de conta para verificação de autorização”. “Rule 01” não ajuda o analista a entender finalidade.

Separe ID da especificação, UUID Sigma e ID local do mecanismo Wazuh. Eles podem apontar para a mesma intenção, mas têm restrições e ciclos diferentes. Documente o vínculo em vez de forçar o mesmo valor em todos os produtos.

## Changelog didático

| Data fictícia | Versão | Alteração | Motivo | Responsável |
| --- | --- | --- | --- | --- |
| 28/09/2026 | 1.0 | Baseline e contexto obrigatório | Tornar criação observável | Equipe LAB |
| Exemplo futuro | 1.1 | Corrigir mapeamento de ator | Parser mudou | Owner LAB |
| Exemplo futuro | 1.2 | Exceção restrita com validade | Provisionamento aprovado | Owner LAB |
| Exemplo futuro | 2.0 | Alterar hipótese para sequência com grupo | Objetivo e dados mudaram | Revisor LAB |

Somente 1.0 é o artefato atual. As outras linhas ilustram possíveis mudanças, não histórico executado. Semantic Versioning é uma opção; revisão por commit ou versão interna também pode funcionar. O requisito é rastreabilidade e capacidade de reproduzir.

## Owner de quê?

Um owner mantém hipótese, dependências, runbook, testes e revisão. Operação de plataforma e triagem podem pertencer a outras pessoas. O contrato deve dizer quem trata erro de coleta, quem aceita risco de exceção e quem pode promover ou reverter a regra.

Sem responsável, ninguém corrige o campo removido, revisa o volume ou encerra a exceção. Um e-mail genérico sem atendimento conhecido não resolve a responsabilidade operacional.

## Revisão e rollback

Reavalie necessidade, fonte, campo, comportamento, infraestrutura, validade das exceções, volume e contexto útil. Cadência depende de risco e ritmo de mudança, não de uma periodicidade universal.

Antes de implantar, guarde versão anterior e dependências. Rollback deve considerar estado, duplicação de alertas, pipelines e exceções, além do arquivo da query. Depois de reverter, teste saúde e resultados conhecidos.

**Entrega:** uma proposta de mudança com diff, justificativa, testes, owner, aprovação e procedimento de reversão. Não publique credenciais junto ao artefato.

## Checkpoint

**Mudar só o nome resolve uma mudança de hipótese?**

<details>
<summary>Ver resposta</summary>

Não. A mudança de hipótese precisa de versão, testes, revisão de escopo e histórico que explique a alteração de comportamento.

</details>

[← Tópico anterior](feedback-to-detections.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](retiring-detections.md)
