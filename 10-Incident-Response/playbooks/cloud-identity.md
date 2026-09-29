# Playbook: identidade cloud suspeita

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)

Identidade cloud pode ser humana, workload, federação ou serviço. Entenda o tipo antes de alterar seu estado. Revogar sessão ou permissão pode quebrar produção, automação ou recuperação.

## Investigar

Identifique principal, tenant/conta fictícia ou escopo, método de autenticação, origem, sessão, permissões e recursos acessados. Revise auditoria disponível para criação de credencial, mudança de papel, consentimento, política e atividade posterior. Verifique atividade esperada com o dono do workload e compare fontes independentes. Registre retenção, atrasos e lacunas.

## Conter proporcionalmente

Avalie revogação de sessão/token, remoção temporária de privilégio, restrição de origem ou suspensão do principal como opções. Para workload, identifique dependências e plano de credencial alternativa seguro. Defina autoridade, duração, monitoramento e reversão. Não compartilhe tokens ou chaves em ticket, chat ou relatório.

## Erradicar e recuperar

Remova credencial ou permissão confirmadamente comprometida, revise relações de confiança e outros principais, aplique correção aprovada e valide por auditoria independente. Atualize segredo de maneira segura se necessário. Retorne serviço com dono e monitore sinais correlatos. Escale exposição de dados e obrigações às áreas competentes.

---

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)
