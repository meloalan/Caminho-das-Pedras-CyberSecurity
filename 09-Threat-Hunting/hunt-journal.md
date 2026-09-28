# Hunt Journal: registro reproduzível

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](hunts.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunt-outcomes.md)

## Identidade do trabalho

Use um ID estável, por exemplo HUNT-WIN-001, sem impor esse formato à organização. Registre título, autor, data, status, motivação e versão. O journal guarda o percurso; o [relatório final](TEMPLATE-RELATORIO-HUNT.md) sintetiza a decisão.

| Bloco | Campos obrigatórios do registro |
| --- | --- |
| Pergunta | Hipótese, alternativas e evidência que fortaleceria/enfraqueceria |
| Limites | Escopo, período, população, timebox e condição de saída |
| Dados | Fontes, cobertura, campos, dataset e versão |
| Pesquisa | Queries, objetivo, filtros, janela, versão e limites |
| Investigação | Pivots, chave, observações, evidências e timeline |
| Decisão | Limitações, conclusão, outcome e responsável |
| Feedback | Detection Gap, Telemetry Gap e próximos passos |

## Registro de cada iteração

| Rodada | Pergunta / query | Resultado observado | Próxima decisão |
| --- | --- | --- | --- |
| Q01 v1 | Falhas/sucessos em WIN-LAB01, 08:00 a 10:00Z | E01/E02/E03/E04/E10 | Separar autoridade antes de correlacionar |
| Q02 v1 | Sessão 0xA100 no mesmo host | E05/E06 | Obter contexto administrativo |
| Q03 v1 | ProcessGuid de E06 | E06/E07/E08 | Registrar DNS-IP não demonstrado |
| Q04 v1 | Relação de E09 com a sessão inicial | Não demonstrada | Manter cadeia de criação separada |

Essas são leituras esperadas dos fixtures, não resultados de execução em produto. Registre seu resultado obtido e divergências em uma cópia do template.

## Integridade e revisão

Preserve evento bruto, identificador, hash do arquivo de evidência quando calculado, comando/query e horário da coleta. Não sobrescreva resultados antigos sem versão. Diferencie exportação original e transformação. Um digest de integridade da evidência não é IOC de malware.

Não guarde apenas query.sql. Anexe contrato de campos, dataset, período e limitações. Se outra pessoa não consegue reproduzir o caminho até a conclusão, o journal ainda está incompleto.

## Exercício

Copie o [TEMPLATE-HUNT](TEMPLATE-HUNT.md), preencha uma rodada e revise com alguém que não conhece o caso. O arquivo antigo [hunts.md](hunts.md) permanece como índice dos packs e ponte para este registro.

## Checkpoint

**O journal deve esconder queries que não retornaram resultados?**

<details>
<summary>Ver resposta</summary>

Não. Elas mostram perguntas testadas e limites. Registre cobertura e o motivo de mudar a próxima pergunta.

</details>

[← Tópico anterior](hunts.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunt-outcomes.md)
