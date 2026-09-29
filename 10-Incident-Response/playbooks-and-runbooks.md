# Playbooks e runbooks

[← Escalonamento](escalation.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Noções de DFIR →](dfir-basics.md)

Uma interpretação didática comum é: playbook descreve coordenação e decisões para uma classe de incidente; runbook detalha uma tarefa técnica. Organizações usam esses termos de maneiras diferentes. O importante é deixar clara a intenção, a autoridade, o risco e o resultado esperado.

## O que um playbook deve conter

1. Escopo, sinais de entrada e critérios locais de classificação.
2. Perguntas para distinguir hipóteses legítimas e adversas.
3. Fontes disponíveis, janela, limitações e preservação de dados.
4. Árvore de decisões e condições para escalar.
5. Opções de contenção, impacto, aprovador, executor e reversão.
6. Erradicação, recuperação, validação e monitoramento.
7. Comunicação, handoff, condições de saída e revisão do próprio playbook.

Não copie lista de comandos sem entender efeito e ambiente. Não execute passo que muda estado de produção sem autorização correspondente. Atualize após mudanças de arquitetura e exercícios.

## Coleção deste módulo

- [Comprometimento de identidade](playbooks/identity-compromise.md)
- [Comprometimento de endpoint](playbooks/endpoint-compromise.md)
- [Phishing](playbooks/phishing.md)
- [Ransomware](playbooks/ransomware.md)
- [Identidade cloud](playbooks/cloud-identity.md)

São guias para discussão e adaptação, não runbooks prontos para produção. Os laboratórios associados são sintéticos.

---

[← Escalonamento](escalation.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Noções de DFIR →](dfir-basics.md)
