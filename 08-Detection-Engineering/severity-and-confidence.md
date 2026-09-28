# Severidade, confiança e prioridade

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](anatomy-of-a-detection.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](false-positives.md)

## Três decisões diferentes

| Conceito | Pergunta | Evidências possíveis |
| --- | --- | --- |
| Severidade | Qual impacto potencial se o comportamento de interesse for confirmado? | Alcance, dados, função do ativo e permissões |
| Confiança | Quão forte é a evidência de que o comportamento de interesse ocorreu? | Campos, vínculos, fonte e hipóteses alternativas |
| Prioridade | Em qual ordem e com qual urgência agir? | Impacto, confiança, criticidade, exposição e fila |

Não existe uma matriz universal de valores neste módulo. As escalas precisam ser acordadas com quem opera e responde. O level de uma regra Wazuh e a magnitude de uma offense QRadar não são números intercambiáveis com severidade do Sentinel.

## Exemplo discutido

Uma conta é criada em um DC sensível. O evento é confiável quanto à criação, mas não informa aprovação. O impacto de uso indevido pode ser alto; a confiança de que a criação foi indevida é baixa. A prioridade pode exigir verificação rápida por causa do ativo, sem afirmar comprometimento.

Se uma mudança aprovada corresponde ao ator, alvo, host e horário, a hipótese adversária perde força. Se a conta entra em grupo sensível sem explicação, existe contexto novo. Documente o que mudou na evidência, e não apenas que o alerta passou de amarelo para vermelho.

## Como registrar a decisão

| Campo | Exemplo fictício |
| --- | --- |
| Severidade inicial | Baixa para baseline de criação, ajustável ao contexto |
| Confiança | Alta no evento de criação; indeterminada quanto à intenção |
| Criticidade | Obtida do inventário, com data de atualização |
| Motivo de priorização | Grupo sensível ou ativo crítico confirmado |
| Próxima ação | Confirmar autorização e expandir timeline |
| Reavaliação | Após novo contexto ou revisão pelo responsável |

**Exercício:** compare criação legítima em DC, criação desconhecida em estação e criação seguida de grupo sensível. Para cada uma, escreva impacto, força da evidência e prioridade separadamente. Não transforme a tabela em escala obrigatória para todos os ambientes.

## Checkpoint

**Baixa confiança permite ignorar sempre um ativo crítico?**

<details>
<summary>Ver resposta</summary>

Não. Criticidade pode justificar investigação rápida. Isso não aumenta automaticamente a certeza nem autoriza contenção sem avaliação.

</details>

[← Tópico anterior](anatomy-of-a-detection.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](false-positives.md)
