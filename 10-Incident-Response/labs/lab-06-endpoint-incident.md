# Lab 06: incidente de endpoint

[← Lab 05](lab-05-identity-compromise.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 07 →](lab-07-phishing.md)

**Objetivo:** integrar timeline, escopo, contenção, evidência e recuperação. **Cenário:** `LAB-WS-17` associado à conta, alerta de processo com confiança baixa. **Arquitetura:** registros sintéticos. **Pré-requisitos:** playbook de [endpoint](../playbooks/endpoint-compromise.md). **Ferramentas:** dataset e templates.

## Execução

1. Correlacione EVT-008 e EVT-009 com autenticações da conta, sem concluir que o processo é malicioso.
2. Liste hipóteses benignas e que exijam contenção; solicite validação do dono e da fonte de endpoint.
3. Defina quais evidências seriam necessárias, quem pode coletar e que efeito isolamento teria.
4. Construa plano de contenção, validação, erradicação e retorno gradual, sem executar ação real.
5. Registre lacunas da cobertura parcial e mensagem de handoff.

**Logs gerados:** nenhum. **Evidências:** escopo e decision log. **Query:** correlacionar entidade, usuário e janela temporal em fonte fictícia. **Regra de detecção:** nenhum ajuste no exercício. **MITRE ATT&CK:** atividade insuficiente para mapear técnica. **Resultado esperado:** tratamento proporcional com confiança indicada. **Resultado obtido:** a preencher.

**O que aprendi:** que dado alteraria a avaliação do endpoint? **Segurança:** sem ferramentas conectadas ou ação em host. **Desafio:** dono informa que o endpoint suporta operação importante. **Referência:** [containment](../containment.md) e [evidence handling](../evidence-handling.md).

---

[← Lab 05](lab-05-identity-compromise.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 07 →](lab-07-phishing.md)
