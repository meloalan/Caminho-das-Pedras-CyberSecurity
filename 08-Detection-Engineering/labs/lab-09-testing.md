# Lab 09: Positivo, negativo e qualidade

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-08-sigma.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-10-detection-as-code.md)

## Objetivo

Executar e criticar uma matriz de testes.

## Cenário

A mudança parece correta no caso positivo, mas pode falhar nas bordas.

## Dados e preparação

Use os testes versionados em detections/tests e os fixtures relacionados.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Quais testes são positive, negative, boundary, null, duplicate e late?
2. Como provar que um teste falha com um defeito?
3. Qual diferença há entre duplicata idêntica e conflito de ID?
4. Qual etapa ainda depende do SIEM?

## Dicas

Faça alterações apenas em cópia de trabalho e reverta o defeito proposital.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

Execute unittest. Em cópia, torne exclusiva a borda inferior; o teste lower_boundary_included deve falhar. Restaure a lógica e execute novamente. ID conflitante é erro de qualidade, não dado a ignorar. Scheduler, parser e entrega do alerta não são exercitados pelo Python e permanecem no plano de integração.

</details>

## Implementação e limites

Use [Testes reproduzíveis com dados fictícios](../testing-detections.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Matriz com comandos, esperado/obtido e limites de teste. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Quais testes são positive, negative, boundary, null, duplicate e late?**

<details>
<summary>Ver resposta</summary>

Execute unittest.

</details>

[← Tópico anterior](lab-08-sigma.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-10-detection-as-code.md)
