# Lab 01: Entendendo campos sem SIEM

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](dados/README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-filtros.md)

## Objetivo

Identificar tipos, papéis e perguntas antes de escrever código.

## Cenário

Você recebeu uma pequena tabela fictícia e precisa decidir o que ela pode responder.

## Dados

E01/E02/E03/E04/E06/E09, na tabela abaixo. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

| ID / UTC | Host | Identidade ou ator/alvo | Provedor / ID | Origem ou processo |
| --- | --- | --- | --- | --- |
| E01 / 08:01 | WIN-LAB01 | LAB/alan.lab | Security-Auditing / 4625 | 192.0.2.10 |
| E02 / 08:02 | WIN-LAB01 | LAB/alan.lab | Security-Auditing / 4625 | 192.0.2.10 |
| E03 / 08:03 | WIN-LAB01 | LAB/alan.lab | Security-Auditing / 4625 | 192.0.2.10 |
| E04 / 08:05 | WIN-LAB01 | LAB/alan.lab | Security-Auditing / 4624 | 192.0.2.10 |
| E06 / 08:08 | WIN-LAB01 | LAB/alan.lab | Sysmon / 1 | powershell.exe |
| E09 / 08:15 | DC-LAB01 | admin.lab → novo.lab | Security-Auditing / 4720 | Não informado |

Este primeiro exercício não exige editor, código nem SIEM. Leia e agrupe as linhas no papel.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Quais colunas existem e quais tipos representam?
2. User é sempre o ator?
3. Qual pergunta pode ser respondida só com essas linhas?
4. Quais informações estão ausentes para afirmar uso não autorizado?

## Dicas

Separe o nome da coluna de seu significado. Timestamp tem fuso; EventID depende do provedor. Conta criada tem ator e alvo diferentes.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

As falhas pertencem a LAB/alan.lab no mesmo host. E09 informa admin.lab como ator e novo.lab como alvo; SourceIP ausente não pode ser preenchido com o endereço de E04. EventID é inteiro no fixture, mas texto em propriedades/index mappings operacionais. Uma pergunta respondível é quantas falhas foram observadas nesse recorte: três. O recorte não contém todas as cinco falhas do dia.

</details>

## Limitações

Não há autorização, resposta DNS ou finalidade de comandos posteriores. A tabela resumida não mostra todos os campos do JSON.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](dados/README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-filtros.md)
