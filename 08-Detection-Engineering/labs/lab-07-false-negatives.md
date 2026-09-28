# Lab 07: Encontre o que a exceção esconde

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-06-tuning.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-sigma.md)

## Objetivo

Produzir um contraexemplo antes de aceitar tuning.

## Cenário

Uma regra ignora qualquer ator cujo nome começa com svc_.

## Dados e preparação

Use registros T061 a T070 do conjunto de tuning.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Esses dez registros são classificados como relevantes no exercício?
2. Por que desaparecem?
3. Qual mudança restrita os preserva?
4. Como testar a validade da exceção?

## Dicas

Não justifique confiança pelo nome da conta. Compare com T001 a T060, o provisionamento aprovado.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

T061-T070 usam svc_backup.lab e são positivos fictícios. O filtro amplo remove o prefixo inteiro. A exceção restrita de svc_provision.lab não corresponde a eles. Teste também mesmo ator em outro host, fora da janela e sem aprovação. Documente risco residual e condição de expiração antes de promover.

</details>

## Implementação e limites

Use [Classificar resultados sem esconder falsos negativos](../false-positives.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Contraexemplo mínimo, teste de regressão e exceção documentada. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Esses dez registros são classificados como relevantes no exercício?**

<details>
<summary>Ver resposta</summary>

T061-T070 usam svc_backup.lab e são positivos fictícios.

</details>

[← Tópico anterior](lab-06-tuning.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-sigma.md)
