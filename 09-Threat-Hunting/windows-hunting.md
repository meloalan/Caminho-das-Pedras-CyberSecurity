# Windows: eventos que respondem perguntas

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](hunting-with-attack.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](sysmon-hunting.md)

## Provedor, canal, versão e resultado

Event ID isolado não identifica universalmente um evento. Use provedor, canal e versão. As referências oficiais estão em [fontes](referencias.md). Para registros de auditoria, confirme também configuração de sucesso/falha e semântica dos campos Subject e Target.

| Pergunta | Eventos | Limite que importa |
| --- | --- | --- |
| Quem tentou e quem autenticou? | 4625 / 4624 | Origem, tipo, host e resultado; credencial válida não prova uso autorizado |
| Houve credenciais explícitas? | 4648 | Tentativa de uso explícito, não prova de logon remoto bem-sucedido |
| Que privilégios chegaram à sessão? | 4672 | Privilégios especiais num novo logon, não mudança de grupo |
| Qual processo foi criado? | 4688 | Command line depende de política; PID pode precisar conversão hexadecimal |
| Houve serviço ou tarefa nova? | 4697 / 4698 | Configuração, ator e ação; execução posterior precisa de evidência própria |
| O que mudou na conta? | 4720 / 4722 / 4723 / 4724 / 4738 | Criação, habilitação, tentativa de troca/reset de senha e alteração de conta |
| Quem entrou em grupo? | 4728 / 4732 / 4756 | Global, local e universal de segurança; autoridade e direitos reais |
| Por que uma conta bloqueou? | 4740 | Caller/contexto e falhas anteriores, sem inferir ataque |
| Como o domínio autenticou? | 4768 / 4769 / 4771 / 4776 | TGT, ticket de serviço, falha de pré-autenticação e validação de credenciais |
| Houve limpeza do Security Log? | 1102 | Provedor Microsoft-Windows-Eventlog, canal Security; não Security-Auditing |

## Pares de campos que não são equivalentes

Ator da criação de conta não é a conta criada. Membro incluído não é o grupo. SubjectLogonId não é automaticamente TargetLogonId. Em 4688, versões podem distinguir contexto criador e contexto alvo; não atribua execução à conta errada. Confirme XML bruto antes de normalizar.

Logon ID deve ser tratado dentro do host e ciclo de inicialização. Em eventos Kerberos, o DC que registrou o evento não é necessariamente o host de origem. Não espere MFA ou informação completa de VPN nesses eventos locais.

## Prática com evidência

E09 registra criação no DC; E14/E15 representam adições em grupos diferentes; E20 registra limpeza. Leia os respectivos campos no [dataset](labs/dados/README.md), separe as identidades e proponha a próxima consulta. Não encadeie esses eventos somente por ocorrerem no mesmo dia.

Investigue o [pack de tarefas e serviços](../hunts/persistence/hunt-09-servico-tarefa.md) com dados sintéticos. Não é preciso criar persistência nem alterar auditoria num sistema real para realizar o exercício.

## Checkpoint

**4672 comprova elevação indevida?**

<details>
<summary>Ver resposta</summary>

Não. Registra privilégios especiais atribuídos a um novo logon. O contexto da conta, da sessão e da autorização precisa ser investigado.

</details>

[← Tópico anterior](hunting-with-attack.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](sysmon-hunting.md)
