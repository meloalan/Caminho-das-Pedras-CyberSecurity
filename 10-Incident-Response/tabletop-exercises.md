# Tabletop exercises

[← Lições aprendidas](lessons-learned.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Playbooks →](playbooks/README.md)

Um tabletop exercita decisões, autoridade, comunicação e coordenação sem executar ações em sistemas reais. Um facilitador apresenta fatos em etapas, participantes explicam o que fariam e um observador registra lacunas. Não é prova individual nem simulação de ataque operacional.

## Preparação

Defina objetivo, participantes, duração, cenário, regras, canal, facilitador e observadores. Declare que todas as contas e eventos são fictícios. Não use credenciais, dados ou infraestrutura de produção. Explique que a equipe pode pausar para esclarecer hipótese e que ninguém deve executar mudança real durante o exercício.

## Roteiro base: identidade privilegiada

1. **Sinal:** chega alerta de autenticação de origem inesperada para `LAB-EXEC`.
2. **Contexto:** a conta tem acesso administrativo e o dono do serviço está ausente.
3. **Incerteza:** titular não foi validado e horário de um log difere do SIEM.
4. **Decisão:** participante compara suspensão, restrição parcial e validação curta com aprovador identificado.
5. **Novo fato:** surge outra sessão em aplicação fictícia, ainda sem prova de uso de dado.
6. **Continuidade:** o grupo define comunicação, prioridade do serviço e critério de retorno.
7. **Handoff:** outro grupo recebe o caso e indica seu próximo passo sem reiniciar a investigação.
8. **Revisão:** equipe converte observações em ações, donos e testes de eficácia.

O facilitador deve evitar revelar solução única. Avalie raciocínio, registro de evidência, escalonamento, consideração de impacto, comunicação e próximo passo.

## Registro de observação

| Momento | Fato apresentado | Pergunta de decisão | Resposta observada | Lacuna | Ação posterior |
| --- | --- | --- | --- | --- | --- |
| 1 | Alerta inicial | Quem valida e quem decide? | A preencher | A preencher | A preencher |

## Segurança e encerramento

Use somente dataset sintético do diretório [labs](labs/README.md). Ao final, recapitule decisões, incertezas e ações. Não use o tabletop para autorizar alteração real. O [lab 09](labs/lab-09-tabletop.md) traz variações com serviço indisponível e comunicação alternativa.

---

[← Lições aprendidas](lessons-learned.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Playbooks →](playbooks/README.md)
