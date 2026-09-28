# Identidade: criação, privilégio e cloud

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](authentication-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](network-hunting.md)

## O que mudou na identidade?

Conta criada, habilitada, senha alterada/resetada, membro adicionado e conta bloqueada são ações distintas. Separe ator, alvo, grupo/papel e autoridade. Pergunte quem concedeu acesso, para quem, quando, em qual sistema, se era esperado e o que a identidade fez depois.

4720 cria conta; 4722 habilita; 4723/4724 registram tentativas de troca/reset de senha; 4738 registra alteração. Resultado e política de auditoria importam. 4728/4732/4756 adicionam membro a grupos global/local/universal de segurança. Nome de grupo não é prova de privilégio efetivo. 4672 informa privilégio na sessão, não a ação de concessão.

## Relação entre criação e atividade

E09 cria LAB/novo.lab por LAB/admin.lab no DC. O suplemento N01 inclui o SID fictício da nova conta em um grupo local de WIN-LAB02; N02 autentica esse SID e N03 registra processo na sessão. C03 documenta a correspondência de nome e SID no inventário sintético. Não confunda a atividade do criador com a atividade da conta criada.

No mundo real, nome pode mudar ou ser reutilizado. Preserve identificador estável, autoridade, vigência e escopo. Sem SID no evento original, declare a dependência do inventário para resolver identidade.

## Além do Windows

Provedores cloud, incluindo Entra ID como exemplo, expõem sign-ins, MFA, dispositivos, aplicações e alterações de papéis. Investigue principal, tenant, aplicação, sessão, resultado e política aplicável. Um evento local Windows não substitui auditoria de identidade cloud.

“Impossible travel” é uma hipótese contextual. VPN, proxies, geolocalização imprecisa, cloud e redes móveis podem explicar localidades distantes. Compare sessões, dispositivos, aplicações e confirmações independentes; não bloqueie com base apenas no mapa.

## Introdução ao cloud hunting

Quem chamou qual API, de onde, em que horário, sobre qual recurso e com qual privilégio? Compare mudanças de configuração com aprovação e atividade posterior. Control plane descreve ações administrativas; investigar execução ou acesso aos dados pode exigir logs de workload/data plane. Confira tenant/projeto/conta, request ID e retenção.

Esses exemplos cloud são roteiro conceitual, sem registros cloud nos fixtures. Uma futura expansão deve declarar seu próprio contrato e população. Consulte [telemetria](hunting-telemetry.md) e o [hunt de grupo](../hunts/identity/hunt-05-grupo-privilegiado.md).

## Checkpoint

**O ator de 4720 é a identidade que deve ser pesquisada como recém-criada?**

<details>
<summary>Ver resposta</summary>

Não. A conta alvo foi criada pelo ator. Investigue cada papel separadamente e use a autoridade e o identificador correto nos pivots.

</details>

[← Tópico anterior](authentication-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](network-hunting.md)
