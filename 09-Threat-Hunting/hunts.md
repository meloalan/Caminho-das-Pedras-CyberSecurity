# Catálogo e registro de hunts

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](multisiem-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunt-journal.md)

## Continuidade do conteúdo original

Este caminho foi preservado. O conceito de registro reproduzível, com consulta, janela, cobertura, achados e decisão, foi ampliado no [Hunt Journal](hunt-journal.md). Ausência de achado continua dependendo de cobertura conhecida.

## Dez hunts completos

| Hunt | Tema |
| --- | --- |
| [HUNT-WIN-001](../hunts/authentication/hunt-01-falhas-sucesso.md) | Falhas seguidas de sucesso |
| [HUNT-WIN-002](../hunts/identity/hunt-02-conta-criada.md) | Conta recém-criada com atividade posterior |
| [HUNT-WIN-003](../hunts/process/hunt-03-processo-incomum.md) | Processo incomum em população conhecida |
| [HUNT-WIN-004](../hunts/process/hunt-04-powershell.md) | PowerShell com contexto de execução |
| [HUNT-WIN-005](../hunts/identity/hunt-05-grupo-privilegiado.md) | Mudança de grupo e privilégio |
| [HUNT-WIN-006](../hunts/identity/hunt-06-log-limpo.md) | Limpeza do log de segurança |
| [HUNT-WIN-007](../hunts/network/hunt-07-processo-conexao.md) | Processo e conexão |
| [HUNT-WIN-008](../hunts/network/hunt-08-dns-processo.md) | DNS e processo |
| [HUNT-WIN-009](../hunts/persistence/hunt-09-servico-tarefa.md) | Serviço ou tarefa criada |
| [HUNT-WIN-010](../hunts/process/hunt-10-administracao-abuso.md) | Administração legítima ou potencial abuso |

## Como escolher

Comece pela pergunta e pelas fontes existentes. Autenticação e identidade exigem papéis bem separados; processo/rede exige chaves de execução; tarefa/serviço exige configuração e evidência de execução. Cada pack possui limites e alternativas próprios.

Use o [exemplo completo](exemplo-hunt-completo.md) para entender o nível de conclusão esperado e os [labs](labs/README.md) para praticar. O [lab integrador original](../12-Labs-Praticos/06-Threat-Hunting/README.md) permanece disponível como exercício complementar.

## Regra de documentação

Guarde versão da consulta e fonte de cada resultado. Classifique a hipótese como sustentada, enfraquecida, refutada no escopo ou inconclusiva. O antigo uso genérico de “confirmado” não deve ser interpretado como incidente confirmado. Status de trabalho e conclusão investigativa são dimensões diferentes.

## Checkpoint

**Onde registrar um hunt depois de escolher o pack?**

<details>
<summary>Ver resposta</summary>

No template e no Hunt Journal, preservando versão, escopo, consultas, resultados obtidos, limitações e outcome. O catálogo não substitui o registro.

</details>

[← Tópico anterior](multisiem-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunt-journal.md)
