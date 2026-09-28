# Cinco casos de uso: do sinal à decisão

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](detection-types.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](anatomy-of-a-detection.md)

## Estrutura de um caso

Nome, objetivo, risco, comportamento, ativo, fonte, campos, hipótese, lógica, entidades, prioridade, resposta, limitações e critério de sucesso devem formar um contrato coerente. O critério de sucesso descreve o que a equipe consegue decidir, não apenas o número de alertas.

## 1. Criação de conta Windows

**DET-WIN-ACCOUNT-001:** observar criação de identidades Windows para verificar autorização e uso posterior. Risco: acesso persistente não aprovado. População inicial: contas locais e de domínio nos hosts/DCs com auditoria e coleta confirmadas.

A seleção inicial é 4720, provedor Security-Auditing, canal Security. Campos: SubjectUserName/Domain, TargetUserName/Domain/Sid, Computer e horário. Preserve EventRecordID quando disponível para rastreabilidade. Identifique quem criou, qual conta foi criada, onde e quando. Não infira escopo só pelo nome da conta: confirme autoridade e papel do host.

A primeira regra é uma baseline de triagem, não uma classificação de criação maliciosa. Mudança aprovada, provisionamento e manutenção são explicações legítimas. A prioridade sobe conforme criticidade, contexto de autorização e atividade relacionada. Consulte grupos posteriores por SID da conta, autenticações e sessão; 4720 não fornece sozinho a origem IP nem comprova privilégio.

**Operação:** encaminhar ao SOC com ator, alvo e referência ao evento. O analista confirma mudança e procura contexto; sem aprovação verificável, mantém a questão aberta. Sucesso do piloto: sinais completos chegam ao responsável, positivos/negativos de laboratório são reproduzidos e o esforço é medido. Falta de fonte ou de contexto deve aparecer na entrega.

A [especificação versionada](../detections/windows/account-management/DET-WIN-ACCOUNT-001.yml) e a [implementação multisiem](multisiem-detection.md) desenvolvem esse caso. O [lab integrador existente](../12-Labs-Praticos/02-EventID-4720/README.md) continua disponível.

## 2. Falhas seguidas de sucesso

**DET-WIN-AUTH-001, proposta didática:** priorizar autenticações que tenham pelo menos três falhas nos dez minutos anteriores ao sucesso. Use conta e autoridade, host de destino, origem e LogonType. O início da janela é inclusivo e o instante do sucesso é excluído das falhas. Três é um parâmetro do fixture, não recomendação universal.

Risco: uso indevido de credenciais. A sequência também pode resultar de senha digitada incorretamente, VPN, serviço com credencial antiga ou recuperação legítima. 4625 + 4624 não comprova brute force bem-sucedido. Se a origem faltar, não junte todos os nulos em uma identidade artificial; registre perda de observabilidade.

**Operação:** consultar usuário, VPN/MFA quando houver fonte, código de falha, ativo e atividade de sessão. 4740 informa bloqueio, não confirma ataque. Compare o teste com uma falha homônima em outra autoridade e com eventos atrasados. Critério: a mesma chave e a ordem corretas sobrevivem a esses controles. Consulte [correlação e query](../07-Buscas-e-Queries-em-SIEM/correlacao-e-joins.md).

## 3. Alteração de membros de grupo sensível

**DET-WIN-GROUP-001, proposta:** investigar inclusão em grupos que o inventário de privilégios classifica como sensíveis. 4728 registra membro adicionado a grupo global de segurança; 4732, grupo local de segurança, incluindo contexto local/domain-local conforme ambiente; 4756, grupo universal de segurança. Nem todo grupo desses tipos concede privilégio relevante.

Campos centrais: SubjectUserName/Domain para ator, MemberSid/MemberName para membro e TargetSid/TargetUserName para grupo. O TargetUserName desses eventos é o grupo, não a pessoa adicionada. Compare SID e autoridade com inventário versionado, evitando lista baseada somente em nomes traduzidos.

**Operação:** conferir quem adicionou, qual membro, grupo, host/DC, horário e aprovação. Investigar autenticação e uso posterior, sem confundir 4672 com inclusão em grupo. Prioridade depende das permissões reais do grupo. Teste grupo comum, grupo sensível, membro não resolvido e mudança autorizada. Critério: reconhecer a mudança relevante sem etiquetar toda associação como escalada.

## 4. Processo e contexto

**DET-WIN-PROC-001, proposta:** identificar uma cadeia que se afasta do perfil documentado do ativo e pede investigação. Fontes possíveis: 4688 com auditoria e campos disponíveis ou Sysmon 1, conforme contrato.

No Sysmon, preserve Image, CommandLine, ParentImage, User, ProcessId, ProcessGuid, ParentProcessGuid e Hashes quando coletados. No 4688, nomes e disponibilidade diferem; use NewProcessName, NewProcessId e campos de pai conforme versão. CommandLine depende da configuração. Não atribua ProcessGuid nativo ao 4688.

**Operação:** validar árvore, conta, assinatura/hash quando disponíveis, função da máquina e mudança aprovada. “powershell.exe” sozinho não satisfaz a hipótese de abuso. O fixture do módulo 07 tem uso de PowerShell compatível com administração; o analista precisa declarar a lacuna de comandos posteriores. Teste nome de ferramenta legítima, cadeia alternativa e comando ausente. Consulte [processos no catálogo](../queries/process-creation/README.md).

## 5. Limpeza do Security Log

**DET-WIN-LOG-001, proposta:** registrar limpeza do log e priorizar preservação/contexto. 1102 usa o provedor Microsoft-Windows-Eventlog no canal Security. Filtrar exclusivamente Security-Auditing apagaria esse sinal.

**Operação:** identificar ator, host e horário; conferir manutenção e continuidade da coleta; expandir timeline com outras fontes. Não provoque limpeza de log real para o exercício. Use dados fictícios ou teste autorizado isolado. Atividade administrativa pode explicar o evento. Critério: o SOC recebe contexto e consegue verificar a lacuna produzida, sem declarar ataque automaticamente. Mapeamento candidato T1070.001 só descreve o comportamento de interesse sob hipótese adversária.

## Mesma pergunta de revisão

Nos cinco casos: o evento ocorreu? O parser trouxe os campos? É esperado nesse ativo? Há autorização verificável? A regra identifica o comportamento ou só uma ferramenta? As [referências oficiais](referencias.md) e o [mapeamento com evidência](mitre-mapping.md) sustentam os contratos.

## Checkpoint

**Uma inclusão em qualquer grupo Windows demonstra novo privilégio administrativo?**

<details>
<summary>Ver resposta</summary>

Não. Primeiro determine o grupo, seu escopo e permissões efetivas. O evento descreve associação; privilégio e intenção precisam de contexto.

</details>

[← Tópico anterior](detection-types.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](anatomy-of-a-detection.md)
