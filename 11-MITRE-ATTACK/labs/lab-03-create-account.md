# Lab 03: Create Account

[← Laboratórios](README.md) · [Técnica](../techniques.md) · [Subtécnicas](../sub-techniques.md)

## Objetivo

Classificar criação de conta com base no contexto, não somente no Event ID.

## Registros fictícios

1. Event ID 4720 observado num endpoint independente, função do host desconhecida.
2. Evento de auditoria com objeto associado ao diretório de domínio confirmado.
3. Audit trail de provedor de identidade cloud confirma criação de usuário.

## Tarefas

1. Para cada registro, marque fato observado, técnica candidata e evidência faltante.
2. Selecione uma subtécnica somente quando o escopo estiver confirmado.
3. Discuta se Persistence é objetivo plausível e o que falta para afirmá-lo.
4. Liste uma fonte complementar e uma hipótese legítima por caso.

## Entrega

Use a página de [subtécnicas](../sub-techniques.md). Para o primeiro caso, não conclua `.001` ou `.002` sem identificar o contexto. Explique que o registro 4720 pode informar criação Windows, mas não resolve sozinho a natureza e intenção do evento.
