# Containment: contenção responsável

[← Registro de decisões](decision-log.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Tratamento de evidências →](evidence-handling.md)

> Conter não significa necessariamente desligar tudo.

Contenção busca limitar propagação, acesso, impacto ou persistência enquanto a equipe investiga e protege a operação. Toda ação deve partir de evidência e contexto, considerar urgência e continuidade, ter autoridade definida e incluir verificação do resultado. Em alguns casos, segurança imediata requer agir antes de coletar tudo. Registre o motivo, a evidência que pode ser perdida e o plano de preservação possível.

## Opções por domínio

| Domínio | Opções conceituais | Efeitos a avaliar |
| --- | --- | --- |
| Identidade | Restringir autenticação, revogar sessão, redefinir credencial, revisar MFA ou privilégio. | Bloqueio do titular, integrações dependentes, sessões que persistem e acesso de emergência. |
| Endpoint | Isolamento controlado, segmentação ou bloqueio de atividade identificada. | Operação crítica, acesso remoto do suporte, evidência volátil e possibilidade de comando ainda ativo. |
| Rede | Restrição de rota ou comunicação específica, segmentação, ACL ou regra de firewall. | Serviços compartilhados, dependências, tráfego legítimo e impacto lateral. |
| Email | Quarentena ou remoção de mensagens identificadas e restrição de remetente conforme contexto. | Mensagens legítimas, cópias, encaminhamento e acesso já realizado. |
| Cloud | Revogar sessão/token, reduzir permissão ou suspender principal conforme arquitetura. | Workloads, automações, dependências, propagação de credenciais e trilha de auditoria. |
| Aplicação/dado | Restringir função, rota ou compartilhamento afetado. | Clientes, transações em andamento, integridade e requisitos de negócio. |

Os termos descrevem classes de opção, não instruções para operar produto. Faça a mudança em ambiente autorizado, por pessoal designado e segundo o procedimento da organização. Um alerta ou IOC isolado não deve acionar contenção automaticamente.

## Perguntas antes da ação

- O que foi observado e qual a qualidade da fonte? A atividade continua?
- Qual identidade, serviço, dado e dependência podem ser afetados?
- Qual dano é plausível se aguardarmos? Qual dano surge se agirmos?
- Há opção mais estreita, reversível ou temporária?
- Quem tem autoridade para aprovar e quem executará?
- É necessário preservar logs, sessão, memória ou outra evidência antes da ação?
- Como verificar a aplicação da contenção e detectar falha?
- Qual é o plano de reversão, responsável, prazo de revisão e critério para remover a medida?
- Quem precisa ser informado para continuidade e comunicação?

## Três alternativas para avaliar

Considere atividade suspeita em `LAB-EXEC`, conta fictícia com privilégio elevado:

1. **Restrição imediata:** limita rapidamente o acesso, mas pode interromper serviço ou resposta legítima. Requer autoridade, confirmação de escopo e plano para dependências.
2. **Restrição parcial e validação paralela:** reduz o caminho suspeito ou revoga sessões específicas enquanto valida titular, aplicações e auditoria. Depende de capacidade técnica e risco residual aceitável.
3. **Monitoramento temporário com prazo curto:** pode preservar atividade observável e evitar interrupção indevida, mas permite que o dano prossiga. Só considerar quando a atividade não mostra dano iminente, com responsável atento, aprovador e gatilho explícito para agir.

Nenhuma opção é resposta universal. Para cada uma documente benefício, risco, evidência preservada ou perdida, impacto, reversibilidade e condição de reavaliação. Se risco de dano ativo for inaceitável, não prolongue observação apenas para obter certeza perfeita.

## Registrar e verificar

Registre estado anterior, ação pedida e executada, alvo, aprovador, executor, horários, confirmação, efeito operacional, evidências impactadas e plano de reversão. Confirme em fonte independente quando disponível. Se a medida falhar, escale e revise a decisão em vez de assumir que o risco foi contido.

---

[← Registro de decisões](decision-log.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Tratamento de evidências →](evidence-handling.md)
