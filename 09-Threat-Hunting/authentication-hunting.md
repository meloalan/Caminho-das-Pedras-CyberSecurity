# Autenticação: da tentativa ao contexto

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](process-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](identity-hunting.md)

## Hipótese e dimensões

Múltiplas falhas seguidas de sucesso podem merecer revisão. Senha digitada incorretamente, credencial antiga numa tarefa, reconexão e automação são alternativas. O sucesso não prova que a pessoa esperada utilizou a credencial.

| Pergunta | Fonte ou campo |
| --- | --- |
| Quem e em qual autoridade? | SID quando disponível, conta, domínio/tenant |
| Em qual host e origem? | Host que registrou, IP de origem e contexto NAT/VPN |
| Qual tipo e motivo? | LogonType, status/substatus e resultado |
| Quantas contas e destinos? | Frequência por identidade/origem, hosts distintos |
| Houve sucesso posterior? | 4624 com chave e janela coerentes |
| Que atividade seguiu? | Sessão, processos, privilégios e mudanças |
| Existe MFA ou VPN? | Logs do provedor correspondente, não inventados no Security |

## Eventos de apoio

4625/4624 descrevem falha/sucesso de logon. 4740 ajuda a investigar bloqueio. 4768/4769 tratam solicitações de tickets Kerberos; 4771 registra falha de pré-autenticação. 4776 registra validação de credenciais, com resultado. Nem todos possuem IP ou host de origem no mesmo campo; respeite o schema.

## Brute force e password spray

Conceitualmente, brute force pode envolver muitas tentativas contra uma conta; password spray pode envolver poucas tentativas contra muitas contas. Distribuição temporal, origem, códigos e contexto importam. Uma contagem de 4625 não mostra senhas tentadas e não confirma nenhuma técnica. Tentativas distribuídas podem não ultrapassar um threshold simples.

## Caso reproduzível

No fixture, E01/E02/E03 antecedem E04 em dez minutos com domínio, conta, host, origem e tipo iguais. E10 é homônimo de outra autoridade e deve ficar separado. E11 pertence a outra conta/host. A observação sustenta uma sequência candidata, não um ataque.

Depois procure 4672 e processo na sessão de E04. A ausência de MFA no arquivo significa dado não fornecido, não que MFA tenha sido ignorada ou desativada. O [hunt 01](../hunts/authentication/hunt-01-falhas-sucesso.md) organiza o roteiro completo e o [multisiem](multisiem-hunting.md) fornece os pontos de entrada.

## Checkpoint

**Três falhas e um sucesso demonstram brute force bem-sucedido?**

<details>
<summary>Ver resposta</summary>

Não. É uma sequência observada compatível com várias explicações. Origem, motivo, identidade, contexto e ações posteriores precisam de análise.

</details>

[← Tópico anterior](process-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](identity-hunting.md)
