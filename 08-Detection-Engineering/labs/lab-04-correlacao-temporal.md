# Lab 04: Ordem, chave e janela

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-03-threshold.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-process-creation.md)

## Objetivo

Validar sequência e limites temporais.

## Cenário

Falhas podem chegar duplicadas, fora de ordem ou depois da primeira execução.

## Dados e preparação

Use E01/E02/E03 e E04 do módulo 07 e os testes locais.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Uma falha exatamente dez minutos antes entra?
2. Uma falha no mesmo instante do sucesso entra?
3. O que ocorre com IP nulo?
4. Como recuperar evento recebido tarde sem repetir alerta?

## Dicas

A janela de falhas é [sucesso-10m, sucesso). A implementação usa relógio original, não ordem de chegada.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

A borda inferior entra; igualdade com o sucesso sai. Uma falha com IP nulo não participa da chave completa e a sequência cai abaixo de três. Duplicata idêntica não aumenta contagem; conflito de ID é erro. O replay tardio recupera a sequência quando reconsidera o histórico, mas o SIEM ainda precisa de política de lookback e estado de alerta. Não declare a sequência brute force confirmado.

</details>

## Implementação e limites

Use [Validar a capacidade, não só a sintaxe](../detection-validation.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Matriz temporal com quatro bordas, atraso e estratégia operacional proposta. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Uma falha exatamente dez minutos antes entra?**

<details>
<summary>Ver resposta</summary>

A borda inferior entra; igualdade com o sucesso sai.

</details>

[← Tópico anterior](lab-03-threshold.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-process-creation.md)
