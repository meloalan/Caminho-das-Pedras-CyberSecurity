# Lab 05: Processo, pai e contexto

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-04-correlacao-temporal.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-tuning.md)

## Objetivo

Desenhar uma seleção de cadeia de processo.

## Cenário

Três registros fictícios mostram PowerShell iniciado por Office, por Explorer e com pai ausente.

## Dados e preparação

Use detections/tests/process-cases.json e office-powershell.sigma.yml. Os dados são normalizados para o exercício, não EVTX.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Qual registro corresponde à condição child and parent?
2. A correspondência prova malware?
3. Como mapear Sysmon 1 e 4688 sem inventar ProcessGuid?
4. O que o caso de pai ausente ensina?

## Dicas

Image e ParentImage são contrato Sigma. No produto, confira fonte e pipeline.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

P01 corresponde; P02 tem pai diferente e P03 não permite satisfazer parent. P01 executa comando administrativo fictício e ainda pode ser legítimo: a seleção identifica cadeia para triagem. Campos ausentes limitam a capacidade. Sysmon pode fornecer GUIDs, enquanto o 4688 exige outro mapping e atenção a PID reutilizado. Valide assinatura, conta, ativo e autorização.

</details>

## Implementação e limites

Use [Sigma: descrição portável, validação específica](../sigma.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Regra experimental, mapa de campos, casos esperados e runbook de contexto. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Qual registro corresponde à condição child and parent?**

<details>
<summary>Ver resposta</summary>

P01 corresponde; P02 tem pai diferente e P03 não permite satisfazer parent.

</details>

[← Tópico anterior](lab-04-correlacao-temporal.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-tuning.md)
