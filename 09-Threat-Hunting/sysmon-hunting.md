# Sysmon: relações de processo e seus limites

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](windows-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](process-hunting.md)

## Perguntas antes da configuração

O [Sysmon oficial](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) registra telemetria; não decide malícia. Eventos dependem de configuração, filtros, versão, disponibilidade e encaminhamento. IDs 3 e 7 são desabilitados por padrão segundo a documentação: instalação não prova cobertura de rede ou módulos.

| ID | Observação | Pergunta e cautela |
| --- | --- | --- |
| 1 | Criação de processo | Qual pai, usuário, comando e ProcessGuid? |
| 3 | Conexão TCP/UDP | Qual processo e destino? Não contém todo payload |
| 7 | Carregamento de imagem/módulo | Que módulo entrou em qual processo? Pode gerar alto volume |
| 8 | CreateRemoteThread | Quem criou thread em outro processo? Contexto legítimo existe |
| 10 | ProcessAccess | Quem abriu outro processo e com quais direitos? Não prova extração de credenciais |
| 11 | FileCreate | Arquivo criado ou sobrescrito; criação não comprova execução |
| 12 | Registro: objeto criado/excluído | Qual chave/valor foi criado ou removido? |
| 13 | Registro: valor definido | Qual valor mudou e por qual processo? |
| 14 | Registro: renomeação | Qual chave/valor mudou de nome? |
| 22 | Consulta DNS | Nome consultado pelo processo, inclusive falhas/cache conforme plataforma |

## Cadeias úteis

ProcessGuid + host liga 1 a 3/22 quando ambos estão disponíveis. ParentProcessGuid permite buscar pai e avô; ausência do evento pai deixa a árvore incompleta. Não trate Image de um evento 7 como o executável criado, pois o evento descreve um módulo carregado.

## Pergunta de investigação

E06/E07/E08 formam uma execução com DNS e conexão no fixture. Não há eventos 7, 8, 10, 11 ou 12 a 14 nesse conjunto. Esses IDs são possibilidades de aprofundamento, não achados do caso.

Confira GUID, host e tempo antes de unir. Um PID reutilizado pode associar a conexão ao processo errado. Hash de arquivo, assinatura e command line complementam o contexto quando presentes; não invente valores ausentes.

## Prática e limite

No WIN-LAB02 não se coletam 3/22 no cenário suplementar. Portanto o processo E12 sem rede observada não pode ser classificado como processo sem comunicação. Registre essa diferença no [journal](hunt-journal.md).

## Checkpoint

**Por que Sysmon 10 não basta para afirmar credential dumping?**

<details>
<summary>Ver resposta</summary>

Porque acesso a processo também ocorre legitimamente. Direitos, origem, alvo, sequência e outras evidências são necessários para investigar a hipótese.

</details>

[← Tópico anterior](windows-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](process-hunting.md)
