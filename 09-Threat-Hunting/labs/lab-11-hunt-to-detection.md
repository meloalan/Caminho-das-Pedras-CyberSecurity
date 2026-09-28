# Transferindo o achado para engenharia

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-10-multisiem-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-final-investigacao-completa.md)

## Objetivo

Produzir candidata acionável com testes e limites.

## Cenário e dados

A sequência E01/E02/E03 → E04 é reproduzível no fixture e merece avaliação operacional.

Use [Hunt to Detection](../hunt-to-detection.md) e o [template do módulo 08](../../08-Detection-Engineering/TEMPLATE-DETECCAO.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Preencha risco, hipótese observável e população.
2. Defina chave completa, janela, threshold didático e tratamento de nulos.
3. Inclua positivo E01/E02/E03/E04 e negativos E10/E11.
4. Adicione duplicata, chegada tardia, limite de tempo e alternativa legítima.
5. Defina owner, runbook, saúde e evidência ainda pendente antes de implantação.

## Perguntas e dicas

O que fazer se o campo necessário não existir? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

Candidata de sequência exige mesma autoridade/conta/host/origem/tipo e falhas anteriores ao sucesso. O threshold três em dez minutos é didático. Privilégios/processo podem ser contexto adicional, não condição inventada como já implementada. Sem teste no SIEM e operação definida, o status é proposta, não detecção pronta.

</details>

## Entrega e critério de conclusão

Parte preenchida do template de detecção, matriz de teste e pacote de evidências do hunt.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**O que fazer se o campo necessário não existir?**

<details>
<summary>Ver resposta</summary>

Registrar telemetry gap e critério de aceite. Não publicar uma detecção que depende silenciosamente de um campo ausente.

</details>

[← Tópico anterior](lab-10-multisiem-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-final-investigacao-completa.md)
