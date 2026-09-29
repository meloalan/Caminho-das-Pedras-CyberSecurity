# Lab 08: recuperação e validação

[← Lab 07](lab-07-phishing.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 09 →](lab-09-tabletop.md)

**Objetivo:** distinguir catálogo de backup de recuperação comprovada. **Cenário:** `BACKUP-LAB-20260928` aparece em EVT-013 e teste simulado EVT-014. **Arquitetura:** revisão de registros fictícios. **Pré-requisitos:** [recovery](../recovery.md). **Ferramentas:** checklist local.

## Execução

1. Compare o catálogo, integridade e resultado de restauração representados.
2. Liste o que ainda precisa validar: origem, escopo, dependência, permissões e dado recente.
3. Defina aprovador de negócio e técnico, ambiente controlado e critério de retorno.
4. Planeje liberação gradual, observabilidade, reversão e janela de monitoramento.
5. Escreva SITREP com limitações. Não afirme que um backup real existe ou foi restaurado.

**Logs gerados:** nenhum. **Evidências:** checklist de retorno e decisão de liberação simulada. **Query:** filtrar `backup_ref`, sem inferir mais que o registro. **Regra:** não aplicável. **MITRE ATT&CK:** não aplicável. **Resultado esperado:** plano verificável e risco residual. **Resultado obtido:** a preencher.

**O que aprendi:** que teste faltaria antes da produção? **Segurança:** sem backup real ou sistema real. **Desafio:** backup antecede a janela suspeita em poucos minutos. **Referência:** [recovery](../recovery.md).

---

[← Lab 07](lab-07-phishing.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 09 →](lab-09-tabletop.md)
