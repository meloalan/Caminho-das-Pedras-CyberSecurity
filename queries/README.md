# Queries por caso de uso

[← Módulo de buscas](../07-Buscas-e-Queries-em-SIEM/README.md) · [Página principal](../README.md)

Escolha primeiro a pergunta, depois a linguagem e o contrato de dados. Os exemplos são educacionais, revisados documentalmente; execução nos produtos depende do ambiente.

| Caso | Conteúdo |
| --- | --- |
| [Autenticação](authentication/README.md) | Falhas em KQL, SPL, AQL e Query DSL no indexer Wazuh |
| [Criação de conta](account-creation/README.md) | Ator, alvo, host e autoridade nas quatro abordagens |
| [Criação de processo](process-creation/README.md) | Sysmon, linhagem e contexto nas quatro abordagens |
| [Correlação temporal](../07-Buscas-e-Queries-em-SIEM/correlacao-e-joins.md) | Chaves, anterioridade, janela e diferenças de mecanismo |
| [Outras perguntas Windows/Sysmon](../07-Buscas-e-Queries-em-SIEM/traduzindo-queries.md) | Grupos, Kerberos, bloqueio, DNS, rede e limpeza do log |

## Arquivos existentes preservados

- [KQL: seis arquivos e explicações](kql/README.md), mantidos para compatibilidade com os labs existentes.
- [Sigma: regra experimental](sigma/README.md).
- [Teste sintético de correlação](tests/README.md).

O catálogo KQL anterior usa cinco falhas como limiar de correlação; o exercício novo usa três. São contratos didáticos distintos. Consultas não implantam regras automaticamente. Configure e teste frequência, lookback, entidades, agrupamento, atrasos e resposta no ambiente alvo.
