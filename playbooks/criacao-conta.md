# Playbook — Criação de conta

[← Playbooks](README.md) · [Página principal](../README.md)

## Entrada

Evento 4720 da [query de criação de conta](../queries/kql/02-conta-criada.md).

## Investigação

1. Distinguir SubjectAccount (ator) e TargetAccount/TargetSid (conta criada).
2. Confirmar se o host é controlador de domínio e se o alvo é local ou de domínio.
3. Verificar aprovação de provisionamento, horário e origem do ator.
4. Investigar adição a grupos, logons posteriores e outros eventos do mesmo ator.
5. Registrar T1136; usar T1136.001 somente após confirmar conta local.

## Decisão

Provisionamento legítimo: documentar o vínculo com a mudança. Criação inexplicada ou privilégio elevado: escalar e avaliar contenção conforme autorização operacional. Não excluir conta só porque ela é nova; pode atender um serviço legítimo.

## Saída

Linha do tempo, escopo confirmado, justificativa MITRE, evidências privadas referenciadas e decisão. O [Lab 02](../12-Labs-Praticos/02-EventID-4720/README.md) fornece um cenário benigno.
