# Packs de Threat Hunting

[← Índice do módulo](../09-Threat-Hunting/README.md) · [Página principal](../README.md)

Dez roteiros reutilizáveis com hipótese, fontes, campos, escopo, seleção inicial, resultados esperados, pivots, alternativas e outcome. Todos usam dados fictícios e leitura defensiva. Nenhum roteiro implanta resposta ou confirma ataque por um sinal isolado.

| Hunt | Pergunta central |
| --- | --- |
| [HUNT-WIN-001](authentication/hunt-01-falhas-sucesso.md) | Falhas seguidas de sucesso |
| [HUNT-WIN-002](identity/hunt-02-conta-criada.md) | Conta recém-criada com atividade posterior |
| [HUNT-WIN-003](process/hunt-03-processo-incomum.md) | Processo incomum em população conhecida |
| [HUNT-WIN-004](process/hunt-04-powershell.md) | PowerShell com contexto de execução |
| [HUNT-WIN-005](identity/hunt-05-grupo-privilegiado.md) | Mudança de grupo e privilégio |
| [HUNT-WIN-006](identity/hunt-06-log-limpo.md) | Limpeza do log de segurança |
| [HUNT-WIN-007](network/hunt-07-processo-conexao.md) | Processo e conexão |
| [HUNT-WIN-008](network/hunt-08-dns-processo.md) | DNS e processo |
| [HUNT-WIN-009](persistence/hunt-09-servico-tarefa.md) | Serviço ou tarefa criada |
| [HUNT-WIN-010](process/hunt-10-administracao-abuso.md) | Administração legítima ou potencial abuso |

## Como reutilizar

Copie o [template](../09-Threat-Hunting/TEMPLATE-HUNT.md), registre versão do pack, dataset, janela, query e resultado obtido. Para outro ambiente, valide o contrato, cobertura e permissões antes de interpretar ausência de resultados. O [dataset](../09-Threat-Hunting/labs/dados/README.md) explicita campos ausentes e janelas.

## Documentação do percurso

O [Hunt Journal](../09-Threat-Hunting/hunt-journal.md) guarda iterações; o [relatório](../09-Threat-Hunting/TEMPLATE-RELATORIO-HUNT.md) comunica a conclusão. Os diretórios authentication, identity, process, network e persistence contêm packs reais, sem pastas reservadas vazias.

[← Índice do módulo](../09-Threat-Hunting/README.md) · [Página principal](../README.md)
