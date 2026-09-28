# Lab 02: Primeira detecção: conta criada

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-01-da-hipotese-aos-dados.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-threshold.md)

## Objetivo

Preencher o template e separar baseline de classificação.

## Cenário

A auditoria de criação de contas está representada por eventos fictícios. Um deles tem ator nulo.

## Dados e preparação

Use detections/tests/account-cases.json e a especificação DET-WIN-ACCOUNT-001.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Qual evento deve corresponder?
2. 4624 deve corresponder?
3. O ator nulo apaga a evidência de criação?
4. Quais partes faltam para operacionalizar?

## Dicas

Compare provider, channel e event_id antes do contexto. A regra é baseline de triagem.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

Os casos 4720 no contrato correspondem; 4624 e provedor errado não. O caso nulo corresponde com missing_context=[actor]. Preencha fonte, hipótese, query vinculada, janela, entidades, impacto/confiança, owner e runbook. Use a implementação multisiem como proposta e deixe execução real pendente.

</details>

## Implementação e limites

Use [Uma especificação de conta criada, quatro implementações](../multisiem-detection.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Template completo, casos esperado/obtido e status experimental. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Qual evento deve corresponder?**

<details>
<summary>Ver resposta</summary>

Os casos 4720 no contrato correspondem; 4624 e provedor errado não.

</details>

[← Tópico anterior](lab-01-da-hipotese-aos-dados.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-threshold.md)
