# Lab 10: Mudança revisável em Git

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-09-testing.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-11-ciclo-completo.md)

## Objetivo

Montar um fluxo de alteração, teste e review.

## Cenário

Você vai substituir uma exclusão ampla pela restrita no exercício fictício.

## Dados e preparação

Use cópia ou branch de estudo, a especificação e o relatório de tuning. Não faça deploy automático.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. O diff mostra somente a mudança pretendida?
2. Quais testes protegem os positivos?
3. O reviewer consegue entender o risco?
4. Como reverter a configuração e as dependências?

## Dicas

O fluxo é branch → alteração → teste → review → merge simulado. Pode registrar tudo sem criar PR público.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

Documente versão-base, alteração, resultado 30 versus 40 alertas e preservação dos dez positivos. Anexe teste de expiração e risco de abuso dentro da janela. O review exige owner, evidência e rollback. Um merge fictício é exercício de governança, não implantação nem aprovação operacional.

</details>

## Implementação e limites

Use [Detection as Code: mudança com evidência e reversão](../detection-as-code.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Diff, comentário de review, changelog e rollback proposto. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**O diff mostra somente a mudança pretendida?**

<details>
<summary>Ver resposta</summary>

Documente versão-base, alteração, resultado 30 versus 40 alertas e preservação dos dez positivos.

</details>

[← Tópico anterior](lab-09-testing.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-11-ciclo-completo.md)
