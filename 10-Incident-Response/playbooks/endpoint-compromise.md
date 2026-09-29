# Playbook: endpoint suspeito

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)

## Entrada e contexto

Receba alerta, relato ou achado de hunting. Preserve identificador, fonte, hora, entidade e conteúdo original. Valide saúde e cobertura de telemetria. Confirme dono, função crítica, usuário, exposição, localização e atividade atual do endpoint. Eventos de processo ou conexão são sinais a contextualizar, não prova automática de comprometimento.

## Investigação e escopo

- Construa timeline de processo, usuário, arquivo, conexões e alterações observadas.
- Relacione a entidade com outras identidades, endpoints e recursos cloud, sem assumir causalidade.
- Compare atividade com software e administração esperados pelo dono.
- Registre limitações de sensor, janela, retenção e horário.
- Preserve dados segundo procedimento antes de ação que os possa alterar, quando isso for compatível com a urgência.

## Contenção

Considere isolamento controlado, segmento restrito ou bloqueio de atividade identificada. Avalie impacto em serviço, segurança física, operações, comunicação e coleta de evidência. Confirme aprovador, executor, alcance, resultado e reversão. Se o risco exigir resposta imediata, escale e documente qual evidência pode ter sido afetada.

## Erradicação e recuperação

Determine causa e persistência com especialista, se necessário. Corrija a causa no escopo confirmado. Reimage ou restauração são opções que exigem fonte confiável, validação de dados e autorização de negócio. Libere gradualmente, monitore recorrência e documente risco residual.

**Saída:** timeline, mapa de escopo, decisão de contenção e recuperação, evidência preservada e handoff. Veja [lab 06](../labs/lab-06-endpoint-incident.md).

---

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)
