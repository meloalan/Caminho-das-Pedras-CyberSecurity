# Automação em Incident Response

[← Noções de DFIR](dfir-basics.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Métricas →](incident-metrics.md)

Automação pode reduzir tarefas repetitivas, mas uma resposta automática sem contexto pode interromper serviço, destruir evidência ou bloquear identidade legítima. Separe enriquecimento reversível de mudança de estado. Use autorização, limites, auditoria e mecanismo de revisão humana conforme o risco.

## Automação de menor risco

Normalizar timestamps, anexar contexto de ativo, agrupar alertas duplicados e preparar rascunho de timeline podem ser bons candidatos, desde que a fonte e a transformação sejam visíveis. Marque claramente saída derivada e permita verificar o registro original.

## Ações que exigem controle reforçado

Suspender conta, revogar sessões, isolar host, bloquear tráfego, apagar mensagem ou alterar serviço pode causar impacto significativo. Antes de automatizar, valide identidade do alvo, qualidade do sinal, exceções, autoridade delegada, janela, reversão, observabilidade, prevenção de repetição e caminho de emergência. Para situações de alto impacto, considere aprovação humana explícita.

## Salvaguardas

- Ambiente de teste e cenários negativos antes de ativação.
- Escopo e allowlist mantidos pelo dono competente.
- Limites de volume e parada de emergência.
- Registro de entrada, decisão, execução, resultado e identidade do aprovador.
- Reavaliação por mudança de processo, fonte ou regra.
- Revisão de falsos positivos e impactos operacionais.

O playbook descreve decisão e autoridade; automação executa apenas o que está formalmente autorizado. Não trate score ou IOC isolado como autorização universal.

---

[← Noções de DFIR](dfir-basics.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Métricas →](incident-metrics.md)
