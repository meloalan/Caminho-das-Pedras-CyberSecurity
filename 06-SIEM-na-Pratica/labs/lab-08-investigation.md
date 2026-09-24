# Lab 08: Investigação do cenário final

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-07-tuning.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-threat-hunting.md)

> Pergunta: qual conclusão é proporcional ao conjunto disponível?

## Objetivo e pré-requisitos

Construir o relatório completo do [cenário final](../investigacao.md), usando o dataset de dez registros. Os eventos são fictícios e não representam incidente real. Leia a tabela de Windows para interpretar 4672 corretamente.

## Execução

1. Execute a análise offline ou leia todas as linhas do dataset.
2. Valide tipos, provider, tempo UTC e identidades.
3. Construa timeline com IDs dos registros como referência.
4. Separe a sequência candidata de autenticação dos eventos de outra autoridade/conta.
5. Relacione sucesso, 4672 e processo apenas pelas chaves fornecidas e com seus limites.
6. Relacione Sysmon 1/3 por ProcessGuid, mantendo dúvida sobre finalidade.
7. Trate a criação de conta por admin-lab como pergunta adicional, não etapa automaticamente atribuída a lab-user.
8. Formule hipóteses concorrentes e três pesquisas adicionais.
9. Classifique com justificativa ou mantenha inconclusivo.
10. Proponha melhoria e um teste que demonstraria seu valor.

## Quatro ambientes

Represente cada pesquisa em Wazuh, SPL, AQL ou KQL conforme a plataforma disponível. Nas demais, declare fonte, campos, filtro, janela e resultado esperado. Nenhuma interface elimina a necessidade de justificar o vínculo entre registros.

## Resultado esperado

Timeline correta, uma sequência candidata de três falhas seguida de sucesso, interpretação de 4672 como privilégio no logon e criação por ator distinto. Não há prova suficiente de ataque confirmado ou benignidade de toda a sequência.

<details>
<summary>Exemplo de conclusão proporcional</summary>

“O conjunto sintético apresenta falhas e sucesso da mesma chave, uma sessão com privilégios e registros de processo/rede relacionados pelos identificadores fornecidos. A finalidade e autorização não foram verificadas. A criação de novo-lab foi registrada sob outro ator e seu vínculo permanece aberto. É necessário obter contexto operacional e fontes adicionais antes de concluir comprometimento ou encerrar todo o conjunto como benigno.”

</details>

## Entrega

Relatório com fatos, hipóteses, consultas, timeline, limitações, próximos passos e responsável fictício. Critério de conclusão: outra pessoa deve conseguir reproduzir a análise e perceber onde a evidência termina.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-07-tuning.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-threat-hunting.md)
