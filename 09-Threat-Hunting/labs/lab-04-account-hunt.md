# Conta criada e atividade posterior

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-03-authentication-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-process-hunt.md)

## Objetivo

Separar ator, alvo, membro e grupo.

## Cenário e dados

Uma conta criada no DC aparece em grupo local e autenticação de outro host.

Use E09/E14, N01/N02/N03 e contexto C03 do [conjunto](dados/README.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Identifique quem criou e quem foi criado em E09.
2. Documente a resolução de identidade feita por C03.
3. Compare grupo global E14 e grupo local N01.
4. Ligue N02/N03 por SID, host e sessão.
5. Solicite aprovação para privilégio e finalidade, sem chamar criação de persistência automática.

## Perguntas e dicas

Pode usar a sessão do criador como sessão da conta criada? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

admin.lab é ator, novo.lab é alvo. C03 fornece SID fictício para a janela. N01 inclui esse SID em Administrators do WIN-LAB02; N02 autentica e N03 cria whoami nessa sessão. E14 tem grupo global cujo nome não prova acesso privilegiado. Uso observado não resolve autorização.

</details>

## Entrega e critério de conclusão

Mapa de identidade e linha do tempo com dependência explícita do inventário.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Pode usar a sessão do criador como sessão da conta criada?**

<details>
<summary>Ver resposta</summary>

Não. São identidades e ações distintas. Pesquise o alvo com seu identificador e encontre sua própria sessão.

</details>

[← Tópico anterior](lab-03-authentication-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-process-hunt.md)
