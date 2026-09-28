# Hunting baseado em comportamento

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](ttps.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunting-with-attack.md)

## A ação sobrevive à troca da ferramenta

Uma nova conta é uma mudança de identidade. GUI, PowerShell, net user e API podem produzir essa mudança, com detalhes de telemetria distintos. Procurar apenas uma command line cobre uma manifestação, não todo o comportamento.

| Pergunta | Observável necessário |
| --- | --- |
| Quem criou a conta? | Ator e identidade alvo separados |
| Em qual autoridade? | Conta local, domínio ou tenant |
| Que acesso recebeu? | Grupo, papel ou política e permissões efetivas |
| Foi usada depois? | SID/identificador estável em autenticações posteriores |
| Era esperado? | Contexto independente de provisionamento e finalidade |

## Previsões e alternativas

Se a hipótese é uso indevido de conta recém-criada, espere criação seguida de atividade incompatível com finalidade conhecida. Onboarding, teste autorizado e automação são alternativas. Ausência de login não refuta intenção futura, e login posterior não comprova abuso.

O [hunt de conta](../hunts/identity/hunt-02-conta-criada.md) distingue ator, alvo e membro de grupo. N01/N02/N03 no suplemento conectam a conta de E09 por SID e sessão. O objetivo é demonstrar relação, não rotular persistência.

## Da busca ao critério

Formule condições observáveis e limites de cobertura. Avalie outras formas de realizar o mesmo comportamento. Se surgir um padrão repetível e acionável, prepare transferência para [Detection Engineering](hunt-to-detection.md), incluindo exemplos legítimos que não devem ser ignorados.

## Checkpoint

**Por que procurar só net user não cobre criação de contas?**

<details>
<summary>Ver resposta</summary>

Porque outras interfaces e APIs realizam a mesma ação. A hipótese deve explicitar se investiga uma ferramenta específica ou o comportamento mais amplo.

</details>

[← Tópico anterior](ttps.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunting-with-attack.md)
