# HUNT-WIN-002: Conta recém-criada com atividade posterior

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)

## Objetivo e hipótese

Relacionar criação, acesso e execução da conta alvo sem atribuir ações ao criador errado.

Se uma nova identidade estiver sendo usada para finalidade indevida, pode receber acesso e executar ações incompatíveis com o provisionamento esperado.

## ATT&CK quando aplicável

T1136.002 é candidata para conta de domínio com finalidade adversária; criação administrativa não confirma persistência. Veja as [referências de mapeamento](../../09-Threat-Hunting/hunting-with-attack.md).

## Fontes e campos

Security 4720, adição em grupo, 4624 e 4688; inventário C03. Campos: ator, alvo, domínio, SID, member_sid, group_sid, host e sessão.

Use o [contrato dos dados](../../09-Threat-Hunting/labs/dados/README.md). Antes de pesquisar, confirme cobertura, retenção, parsing, nulos e limites. As saídas abaixo são resultados esperados dos arquivos fictícios, não execução em SIEM.

## Escopo e condição de saída

LAB/novo.lab, DC-LAB01 e WIN-LAB02, [08:00Z, 10:00Z) de 24/09/2026.

Encerrar ao responder aos pivots ou documentar a fonte/contexto que impede a decisão. Uma expansão exige justificativa e nova janela registrada.

## Query inicial e resultado

**Pergunta/seleção no contrato normalizado:** Selecionar Security-Auditing/event_id 4720 no período; preservar ator e alvo separados. Buscar depois o SID resolvido por C03 em membro e usuário.

**Resultado esperado:** E09 cria novo.lab por admin.lab. E14 adiciona o membro a grupo global, sem privilégio demonstrado pelo nome. N01 adiciona ao grupo local Administrators no WIN-LAB02; N02/N03 mostram logon e processo.

Adapte a consulta usando [KQL/SPL/AQL/Query DSL](../../09-Threat-Hunting/multisiem-hunting.md) e os contratos do módulo 07. O filtro em prosa é uma especificação de pesquisa, não uma linguagem executável universal.

## Pivots e interpretação

1. Resolver a conta alvo por C03 e registrar dependência do inventário.
2. Examinar N01: grupo SID S-1-5-32-544 local ao host, ator admin.lab.
3. Relacionar N02/N03 pelo SID e sessão 0xB200 no WIN-LAB02.
4. Procurar aprovação de onboarding e finalidade; não inferir relação com E04.

## Explicações alternativas e limitações

Onboarding, teste e conta temporária são alternativas. Não há confirmação de autorização dos privilégios. O processo whoami é benigno no fixture, mas não explica toda a finalidade.

Preserve a distinção entre relação sustentada por chave, proximidade temporal e inferência de intenção. Ausência de campo ou de resultado pode deixar a hipótese inconclusiva.

## Conclusão e outcome possível

Criação e uso estão observados; finalidade indevida inconclusiva. Registrar revisão de privilégio e candidata de contexto de conta nova, com exceções delimitadas.

Registre observação, inferência, conclusão e próximo responsável no [Hunt Journal](../../09-Threat-Hunting/hunt-journal.md). Uma candidata deve seguir [Hunt to Detection](../../09-Threat-Hunting/hunt-to-detection.md), com positivos, negativos e limites explícitos.

## Checkpoint

**Qual evidência ainda falta para decidir a finalidade?**

<details>
<summary>Ver resposta</summary>

Volte às alternativas deste pack e identifique o dado que as separa. Os registros sustentam observações específicas, mas não autorizam ampliar a conclusão além da cobertura ou tratar o sinal como ataque automático.

</details>

[← Catálogo de hunts](../README.md) · [Índice do módulo](../../09-Threat-Hunting/README.md) · [Página principal](../../README.md)
