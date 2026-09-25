# Dataset sintético: contrato e resultados

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](../README.md) · [↑ Índice do módulo](../../README.md) · [Página principal](../../../README.md) · [Próximo tópico →](../lab-01-entendendo-campos.md)

## Conteúdo

[eventos.jsonl](eventos.jsonl) contém 22 objetos fictícios, um por linha. IDs E01 a E20 pertencem a 24/09/2026; H01/H02 pertencem ao dia anterior. O arquivo não está ordenado cronologicamente. [inventario.csv](inventario.csv) contém quatro hosts esperados. [analisar.py](analisar.py) permite conferência offline.

## Tipos e semântica

| Campo | Tipo | Papel |
| --- | --- | --- |
| id | string | Identificador único do fixture, não EventRecordID nativo |
| synthetic | boolean | Indica dado fictício |
| timestamp | string ISO 8601 UTC, convertida para datetime | Ocorrência didática |
| provider / event_id | string / inteiro | Identidade do tipo de evento |
| host | string | Host original |
| user / domain | strings opcionais | Conta observada; alvo na criação, identidade no processo |
| actor / actor_domain | strings opcionais | Autor da operação |
| source_ip / destination_ip | strings IPv4 opcionais | Papéis separados de rede |
| logon_type / process_id | inteiros opcionais | Tipo de logon / PID local |
| logon_id / process_guid | strings opcionais | Chaves no contexto do host e execução |
| image / parent_image / command_line | strings opcionais | Processo e linha de criação |
| privileges | array opcional | Privilégios registrados no exemplo |
| query_name | string opcional | Nome consultado, sem resposta DNS |

Campo ausente não deve ser preenchido por aproximação temporal. E09 não fornece IP. E14 usa grupo global, E15 grupo local; nome de grupo global não comprova privilégio. E20 tem provider Eventlog, embora pertença ao canal Security. 4688 E13 usa PID decimal normalizado no fixture, enquanto payload nativo pode usar representação hexadecimal.

## Resultados esperados

| Pergunta | Resposta no fixture |
| --- | --- |
| Registros totais / atuais | 22 / 20 |
| Falhas atuais | 5 |
| Falhas por host | WIN-LAB01: 4; WIN-LAB02: 1 |
| Falhas por identidade | LAB/alan.lab: 3; OUTRO/alan.lab: 1; LAB/svc.lab: 1 |
| Sucessos atuais | E04 |
| Sequência candidata | E01/E02/E03 antes de E04 |
| Sysmon 1 atuais | E06/E12 |
| Sysmon da execução E06 | E06/E07/E08 |
| Conta criada | E09, ator admin.lab, alvo novo.lab, domínio LAB |
| Fonte esperada sem registros | WIN-LAB03 |

## Limites intencionais

Dois dias não formam baseline confiável. Não há hashes, resposta DNS, prova de autorização ou comandos interativos posteriores. PowerShell E06 usa -NoExit para permanecer aberto; a conexão posterior é observação sintética, não uma consequência atribuída a Get-Date. E12 e E13 representam a mesma criação por fontes distintas. Nunca some fontes como se cada registro representasse execução diferente.

IPs 192.0.2.0/24 e 198.51.100.0/24 são reservados para documentação; example.test é domínio de teste. Não há endpoints reais a consultar. O analisador só lê arquivos locais.

## Uso em plataformas

As queries operacionais usam schemas nativos e aliases/propriedades declarados no [contrato](../../campos-e-schemas.md). Para importar o JSON, crie um dataset customizado de laboratório e adapte nomes/tipos; não declare que essa importação aconteceu. O exercício KQL datatable em [fundamentos](../../fundamentos-de-consulta.md) é autossuficiente e separado.

## Checkpoint

**Por que os resultados do fixture não comprovam execução nos SIEMs?**

<details>
<summary>Ver resposta</summary>

O fixture usa um contrato próprio. Ele testa raciocínio e cálculo; cada produto precisa de ingestão, campos e execução verificados.

</details>

[← Tópico anterior](../README.md) · [↑ Índice do módulo](../../README.md) · [Página principal](../../../README.md) · [Próximo tópico →](../lab-01-entendendo-campos.md)
