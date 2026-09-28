# Lab 01: Da hipótese aos dados

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-primeira-deteccao.md)

## Objetivo

Traduzir uma demanda em contrato, antes de escrever código.

## Cenário

O responsável por WIN-LAB01 quer saber quando uma conta é criada fora do fluxo aprovado. Você ainda não tem logs nem lista de mudanças.

## Dados e preparação

Nenhum SIEM é necessário. Use papel ou um documento; leia o caso 1 em casos-de-uso.md.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Qual comportamento observável representa a demanda?
2. Qual fonte, evento e campos seriam necessários?
3. Qual contexto distingue criação legítima e criação a investigar?
4. Qual ação o SOC pode tomar sem bloquear automaticamente?

## Dicas

Separe fato registrado e autorização externa. Não comece por “4720 = ataque”.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

A hipótese pede verificar criação de conta, autoridade e aprovação. Security 4720 pode registrar ator e alvo; o ticket e a finalidade vêm de contexto independente. Defina host/DC, horário, retenção e auditoria. O SOC confere autorização e procura grupos/logons posteriores. Antes de qualquer query, entregue fonte, campos, comportamento legítimo semelhante e lacunas.

</details>

## Implementação e limites

Use [Hipóteses que podem ser testadas](../detection-hypothesis.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Uma especificação de uma página com hipótese e evidência contrária. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Qual comportamento observável representa a demanda?**

<details>
<summary>Ver resposta</summary>

A hipótese pede verificar criação de conta, autoridade e aprovação.

</details>

[← Tópico anterior](README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-primeira-deteccao.md)
