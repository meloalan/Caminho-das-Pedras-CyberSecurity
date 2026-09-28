# Da conta ao grafo de entidades

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-05-process-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-baseline-rarity.md)

## Objetivo

Criar um mapa de relações sustentadas e relações não demonstradas.

## Cenário e dados

A pista inicial é LAB/alan.lab, sem IOC confirmado.

Use E01 a E10 e a página [pivoting](../pivoting.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Conta/domínio → autenticação e host.
2. Host/sessão → privilégios e processo.
3. Host/ProcessGuid → DNS e conexão.
4. Marque a ausência de resposta DNS.
5. Avalie se E09 pode entrar na mesma cadeia e justifique a decisão.

## Perguntas e dicas

Qual chave usar para unir eventos Sysmon da mesma execução? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

O mapa chega a E04, E05, E06 e depois E07/E08. Não há aresta comprovada domínio → IP. E09 é outra cadeia, em outro host e com outro ator/alvo. E10 não é a mesma identidade. Cada aresta precisa de IDs e chave, não só uma seta bonita.

</details>

## Entrega e critério de conclusão

Grafo com rótulos de relação, IDs e uma lista de associações recusadas.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Qual chave usar para unir eventos Sysmon da mesma execução?**

<details>
<summary>Ver resposta</summary>

ProcessGuid e host no contexto da fonte, com tempo coerente. PID sozinho pode ser reutilizado.

</details>

[← Tópico anterior](lab-05-process-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-baseline-rarity.md)
