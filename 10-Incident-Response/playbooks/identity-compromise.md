# Playbook: suspeita de comprometimento de identidade

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)

## Objetivo e entrada

Avaliar atividade inesperada em uma identidade e limitar acesso proporcionalmente, sem presumir que localização ou indicador isolado provam abuso. Entrada: alerta, relato do titular ou evidência de sessão suspeita. Aplique critérios e autoridade locais. Exemplo: `LAB-EXEC`, identidade executiva fictícia.

## Validar e ampliar contexto

1. Preserve o alerta original, evento, fonte, horário e fuso; separe event time de ingestão e detecção.
2. Confira saúde, cobertura e retenção do provedor de identidade e aplicações.
3. Verifique origem, dispositivo, método e resultado de autenticação forte, aplicação, sessão e privilégios. Geolocalização é aproximada.
4. Procure eventos relevantes próximos: falhas e sucessos, novos fatores, redefinições, alteração de grupo ou privilégio, consentimento, sessão e acesso a aplicações.
5. Confirme com titular por canal independente e previamente verificado. Não use a sessão possivelmente suspeita.
6. Expanda escopo a outras sessões, contas, dispositivos, aplicações e recursos relacionados.
7. Registre fatos, hipóteses, desconhecidos, confiança e pergunta seguinte.

## Decidir contenção

Se houver sessão ativa com evidência corroborada, privilégio elevado ou impacto plausível em curso, escale de acordo com urgência e autoridade. Avalie suspensão, revogação de sessão, restrição temporária, redefinição de credencial e revisão de fatores. São opções, não sequência obrigatória. Considere integrações, serviços e acesso de emergência; planeje efeito, verificação e reversão. A redefinição sozinha pode não encerrar sessões já existentes.

Antes de ação, pergunte quem aprova, que serviço pode falhar, que evidência se perde, se há opção mais estreita e como validar o estado. Se esperar for perigoso, aplique a medida autorizada proporcional e registre limitações. Não mantenha observação sem prazo enquanto dano plausível continua.

## Erradicar, recuperar e fechar

Após limitar risco, investigue mudança de credencial/fator, sessão persistente, privilégio ou aplicação. Corrija causa confirmada, revise acessos relacionados e valide atividade por fonte independente. Restaure serviços dependentes com donos informados. Monitore sinais relacionados e registre risco residual. Acione jurídico/privacidade se fatos indicarem possível dado pessoal, sem concluir obrigação automaticamente.

## Saída e handoff

Registre timeline, entidades, evidências e limites, decisão e aprovação, estado atual, próximo passo, responsável e gatilho de escalonamento. Use [templates](../TEMPLATE-INCIDENTE.md) e [lab 05](../labs/lab-05-identity-compromise.md).

---

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)
