# Eventos Windows: perguntas antes dos números

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](traduzindo-entre-siems.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](sysmon-wef.md)

## Identifique a fonte completa

Event ID só faz sentido junto com provider, canal, versão e contexto. Security usa `Microsoft-Windows-Security-Auditing`; Sysmon usa outro provedor e canal. Os eventos disponíveis dependem de auditoria, versão, configuração e coleta. Instalar um agente não habilita automaticamente todas as subcategorias.

## Security

| ID | O que representa | Pergunta útil | Limite |
| --- | --- | --- | --- |
| 4624 | Logon bem-sucedido | Qual conta, tipo de logon, host e sessão? | Não prova presença física nem legitimidade. |
| 4625 | Falha de logon | Qual alvo, origem, LogonType e status/substatus? | Não significa automaticamente tentativa maliciosa. |
| 4634 | Sessão de logon encerrada | Qual Logon ID terminou neste host? | Compare sessão e escopo; não mede toda atividade da pessoa. |
| 4648 | Uso de credenciais explícitas | Qual processo tentou usar outra identidade? | Não comprova que o destino aceitou a autenticação. |
| 4672 | Privilégios especiais atribuídos a novo logon | Qual sessão recebeu privilégios sensíveis? | É comum para identidades de sistema; não é adição a grupo. |
| 4688 | Processo criado | Qual imagem, pai, conta e comando? | Command line exige configuração adicional e pode estar ausente. |
| 4697 | Serviço instalado no sistema | Quem instalou qual serviço? | Depende de auditoria; não equivale ao 7045 do canal System. |
| 4698 | Tarefa agendada criada | Quem criou e qual definição foi registrada? | Uma tarefa pode ser legítima; inspecione conteúdo e contexto. |
| 4720 | Conta de usuário criada | Quem criou, qual alvo e autoridade? | Conta local e de domínio exigem contexto do host/DC. |
| 4722 | Conta habilitada | Quem habilitou qual conta? | Habilitação não demonstra uso posterior. |
| 4724 | Tentativa de redefinição de senha | Qual ator e alvo, com qual resultado auditado? | Não confundir reset com alteração da própria senha. |
| 4728 | Membro adicionado a grupo global de segurança | Qual membro e qual grupo no domínio? | Não é o evento de todo tipo de grupo. |
| 4732 | Membro adicionado a grupo local de segurança | Qual membro, grupo e autoridade? | Grupo local/domain local precisa de contexto. |
| 4738 | Conta de usuário alterada | Quais atributos foram registrados como alterados? | Alguns campos podem não informar todas as diferenças. |
| 4740 | Conta bloqueada | Qual conta e computador de origem quando informado? | Pode ser credencial antiga de serviço. |
| 4768 | Solicitação de TGT Kerberos | Qual principal e resultado no DC? | Verifique versão e campos de criptografia/resultado. |
| 4769 | Solicitação de ticket de serviço Kerberos | Qual serviço, principal e resultado no DC? | Solicitação não prova utilização do recurso. |
| 4771 | Pré-autenticação Kerberos falhou | Qual conta, cliente e código de falha? | Fonte típica é DC; código precisa de contexto. |
| 4776 | Validação de credenciais | Qual conta e resultado da validação NTLM? | Host que valida e workstation não são campos intercambiáveis. |
| 1102 | Log de auditoria limpo | Qual identidade limpou Security e quando? | Pode ser manutenção autorizada; merece contexto e preservação. |

Consulte o [catálogo Microsoft de auditoria avançada](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-auditing) para selecionar a subcategoria correta. O [4625 oficial](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) detalha campos e códigos. O [4720 oficial](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720) ajuda a separar Subject e Target.

## Sysmon

| ID | Tipo | Pergunta útil | Limite |
| --- | --- | --- | --- |
| 1 | ProcessCreate | Pai, imagem, comando, hashes e ProcessGuid | Não prova finalidade ou toda atividade posterior. |
| 3 | NetworkConnect | Qual processo se associou a comunicação TCP/UDP? | Não é captura de pacotes nem registro genérico de ICMP. |
| 7 | ImageLoad | Qual módulo foi carregado por um processo? | Pode gerar alto volume e requer configuração. |
| 8 | CreateRemoteThread | Qual processo criou thread em outro? | A relação não determina sozinha a intenção. |
| 10 | ProcessAccess | Qual processo acessou outro e com que direitos? | Precisa de filtros e contexto; ferramentas legítimas também acessam processos. |
| 11 | FileCreate | Qual processo criou/sobrescreveu arquivo observado? | Não é prova de leitura ou de conteúdo malicioso. |
| 12/13/14 | RegistryEvent | Objeto criado/removido, valor alterado ou nome alterado? | Distinguir tipo de operação e objeto. |
| 22 | DNSQuery | Qual processo consultou um nome? | Consulta não prova conexão concluída. |

A [documentação Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) explica eventos e configuração. Registre quais tipos estão habilitados: ausência de Sysmon 3 ou 7 com filtro desabilitado não demonstra ausência de rede ou módulo carregado.

## Chaves para correlação

Para sessões, compare host, conta/autoridade e Logon ID quando aplicável. O TargetLogonId do 4624 pode relacionar-se ao SubjectLogonId de outro evento no mesmo host, mas não é um identificador global entre máquinas. Falhas 4625 não devem receber por inferência o Logon ID do sucesso posterior.

Para processos, prefira ProcessGuid quando disponível, host e tempo de início. PID pode ser reutilizado. Para registros, EventRecordID precisa de canal, host e contexto de rotação; não é uma chave global. Para rede, confirme que a fonte relaciona processo e conexão e cobre o protocolo em questão.

## Prática

Escolha 4625, 4720 e Sysmon 1. Para cada um, escreva uma pergunta respondível, cinco campos necessários e uma conclusão que o evento não sustenta sozinho. Use os [labs de autenticação](labs/lab-03-windows-authentication.md), [criação de usuário](labs/lab-04-user-creation.md) e [processos](labs/lab-05-sysmon-process-creation.md).

## Checkpoint

**4672 indica que alguém adicionou uma conta a Administradores?**

<details>
<summary>Ver resposta</summary>

Não. Indica privilégios especiais atribuídos ao novo logon. Mudanças de membros de grupo exigem eventos correspondentes.

</details>

**Event ID 1 identifica unicamente Sysmon?**

<details>
<summary>Ver resposta</summary>

Não. É necessário provider e canal, além da configuração e versão.

</details>

[← Tópico anterior](traduzindo-entre-siems.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](sysmon-wef.md)
