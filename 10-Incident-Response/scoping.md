# Escopo

[← Timeline](incident-timeline.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Registro de decisões →](decision-log.md)

Uma pergunta central é se o primeiro ativo observado é o único afetado. Escopo orienta contenção, prioridade, comunicação e recuperação. Expanda de forma dirigida por hipótese e evidência, registrando o limite de cada fonte. “Não encontramos” só é informativo se a busca tinha cobertura e janela adequadas.

## Pivôs de investigação

```text
Identidade → sessões → aplicações → dispositivos → privilégios
Host → usuário → processo observado → conexões → outros hosts
Mensagem → destinatários → interação reportada → identidade → endpoint
Recurso cloud → principal → sessão/token → permissões → recursos acessados
```

São caminhos de pergunta, não indicação de atividade maliciosa. Um indicador pode ser compartilhado por serviços legítimos ou infraestrutura intermediária. Correlacione timestamp, entidade e fonte, em vez de bloquear apenas por correspondência de string.

## Matriz de escopo

| Entidade | Relação com o caso | Evidência | Estado | Limitação | Próxima busca |
| --- | --- | --- | --- | --- | --- |
| `LAB-EXEC` | Conta no alerta | Registro IdP sintético | Confirmada no alerta | Titular não validado | Revisar sessões e atividade posterior |
| `LAB-WS-17` | Dispositivo associado | Inventário fictício | Possível | Telemetria parcial | Validar com endpoint owner |
| `APP-LAB-FIN` | Aplicação acessível | Mapa de privilégios fictício | Confirmada como dependência | Acesso efetivo ainda não demonstrado | Consultar auditoria de aplicação |

Use estados como confirmado, provável, possível, descartado e desconhecido, com critérios locais. “Confirmado” sempre deve dizer exatamente o que foi confirmado, por qual fonte e em qual período.

## Escopo e decisão de contenção

Não espere um mapa perfeito se a atividade estiver ativa e o dano potencial for alto. Registre a incerteza e considere uma medida proporcional enquanto continua a investigação. Se a contenção puder interromper serviço crítico, mobilize dono técnico e de negócio. Decida se o ganho de limitar dano supera o custo de perda de disponibilidade ou evidência. Inclua alternativa menos disruptiva, reversão, aprovador e gatilho de reavaliação no [log de decisão](decision-log.md).

## Critérios para concluir a busca

Não há limite universal de “escopo concluído”. Declare quais fontes, entidades e janelas foram cobertas, quais estão fora da telemetria e que evidência sustenta o limite. Uma busca incompleta permanece uma limitação explícita, não prova de ausência.

**Entrega:** mapa de entidades, relações, status de confirmação e lacunas para o [lab 03](labs/lab-03-scoping.md).

---

[← Timeline](incident-timeline.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Registro de decisões →](decision-log.md)
