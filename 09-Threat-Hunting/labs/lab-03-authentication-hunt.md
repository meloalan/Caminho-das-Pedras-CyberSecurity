# Falhas, sucesso e hipóteses concorrentes

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-02-validando-telemetria.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-account-hunt.md)

## Objetivo

Construir uma sequência candidata sem misturar homônimos.

## Cenário e dados

Falhas de alan.lab aparecem perto de um sucesso em WIN-LAB01.

Use E01 a E11 do [dataset original](../../07-Buscas-e-Queries-em-SIEM/labs/dados/eventos.jsonl) e o [hunt 01](../../hunts/authentication/hunt-01-falhas-sucesso.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Escreva hipótese e alternativa de erro de digitação.
2. Selecione falhas/sucessos do host na janela principal.
3. Separe domain, user, source_ip e logon_type.
4. Para E04, procure falhas nos dez minutos anteriores.
5. Faça pivot para sessão e registre o que ainda falta para avaliar abuso.

## Perguntas e dicas

Qual seria o efeito de agrupar só pelo nome alan.lab? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

E01/E02/E03 antecedem E04 com a mesma chave. E10 é OUTRO/alan.lab e não entra; E11 é outra conta/host. E05/E06 oferecem contexto da sessão. Três falhas e sucesso sustentam a sequência, não brute force nem comprometimento. Falta confirmação independente da finalidade.

</details>

## Entrega e critério de conclusão

Tabela de seleção, chave de correlação e duas conclusões: sequência observada; intenção inconclusiva.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Qual seria o efeito de agrupar só pelo nome alan.lab?**

<details>
<summary>Ver resposta</summary>

Somaria E10 de outra autoridade e fabricaria uma contagem maior para LAB/alan.lab.

</details>

[← Tópico anterior](lab-02-validando-telemetria.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-account-hunt.md)
