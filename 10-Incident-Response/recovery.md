# Recovery: recuperação confiável

[← Erradicação](eradication.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Encerramento →](closure.md)

Recuperar é devolver serviços a estado confiável com autorização, validação e monitoramento. Pressão por disponibilidade não deve ocultar causa não removida. Inversamente, manter contenção além do necessário pode aumentar dano operacional. O dono do negócio e os responsáveis técnicos participam da decisão de retorno.

## Critérios de retorno

- A causa conhecida foi removida ou mitigada com controle residual aprovado.
- A origem de restauração é confiável, íntegra e adequada ao objetivo.
- Dependências, identidade, segredos e permissões foram revisados.
- Funcionalidade, segurança e integridade dos dados foram verificadas.
- A contenção pode ser retirada gradualmente e com plano de reversão.
- Há responsável de negócio, operador e pessoa que monitora o retorno.
- Usuários e stakeholders relevantes conhecem o estado e limitações.

## Backup não é sinônimo de recuperação

Confirme origem, data, integridade, escopo e exposição do backup. Avalie se contém a causa ou dados alterados durante o incidente. Teste restauração em ambiente controlado e valide funcionalidade, permissões e integridade antes da liberação. Não conecte uma restauração não verificada a ambientes de produção. Os objetivos RTO/RPO e critérios de negócio pertencem ao plano de continuidade da organização.

## Retorno gradual

Quando arquitetura permitir, restaure por etapas: validar ambiente controlado, liberar escopo limitado, confirmar sinais esperados, ampliar acesso e manter monitoramento reforçado. Defina previamente condição para interromper ou reverter. Um alerta após retorno exige avaliação; não significa automaticamente recorrência, e a ausência de alerta não prova que o problema acabou.

## Monitoramento pós-retorno

Acompanhe as mesmas entidades e hipóteses relevantes, além de integridade, autenticação, disponibilidade e efeitos ao usuário. Registre janela e fontes monitoradas, lacunas, responsável, critérios de escalonamento e condição para encerrar monitoração reforçada. A duração depende de risco e política local.

**Entrega:** plano de retorno para serviço fictício com critérios, aprovações, validação, monitoramento e reversão. O [lab 08](labs/lab-08-recovery.md) usa um inventário sintético de backup.

---

[← Erradicação](eradication.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Encerramento →](closure.md)
