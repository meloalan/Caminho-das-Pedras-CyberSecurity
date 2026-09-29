# Playbook: phishing reportado

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)

## Entrada

Receba mensagem suspeita, alerta de gateway ou relato de usuário. Preserve identificador da mensagem e cabeçalhos por canal seguro, com minimização de dados. Não clique em links ou anexos para “testar”. Use ambiente e métodos autorizados.

## Escopo

1. Determine quem recebeu e em que janela, usando telemetria disponível.
2. Verifique se alguém interagiu, por confirmação segura e sinais técnicos autorizados.
3. Se houve interação, investigue identidade e endpoint relacionados, sem assumir infecção.
4. Procure mensagens correlatas e encaminhamentos; valide limites de entrega e retenção.
5. Avalie conteúdo e possível dado exposto com equipes apropriadas.

## Decisões de resposta

Quarentena ou remoção, bloqueio de remetente/domínio e revogação de sessão dependem de confirmação, alcance, impacto e autoridade. Um domínio compartilhado pode hospedar tráfego legítimo. Remova mensagens identificadas conforme processo, confira cópias e encaminhamentos, valide o efeito e documente exceções. Se uma conta ou endpoint estiver potencialmente afetado, siga o playbook correspondente.

## Fechamento

Registre quantidade e escopo cobertos, usuários contatados, ações e resultado, lacunas e eventual encaminhamento de privacidade. Oriente usuários por mensagem aprovada, sem expor destinatários. Use dados sintéticos no [lab 07](../labs/lab-07-phishing.md).

---

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)
