# Detecção e análise

[← Papéis e responsabilidades](roles-and-responsibilities.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Classificação e severidade →](classification-and-severity.md)

Detecção inicia uma avaliação, não determina sozinha que houve comprometimento. A análise compara hipóteses com evidência, contexto do ativo, identidade, atividade relacionada e qualidade da fonte. Uma consulta deve responder a uma pergunta operacional: existe sessão ativa? Outros hosts tiveram a mesma atividade? A mudança foi autorizada? Cada busca deve ter janela temporal, entidade, fonte e resultado registrados. Para sintaxe e operadores, consulte os [módulos de SIEM e queries](../06-SIEM-na-Pratica/README.md) e [buscas](../07-Buscas-e-Queries-em-SIEM/README.md).

## Triagem inicial

1. Registre alerta ou relato como recebido, sem promover automaticamente a incidente.
2. Preserve identificador, regra, fonte, hora de evento, hora de ingestão e hora de detecção quando disponíveis.
3. Verifique se a fonte estava saudável, se o dado está completo e qual fuso é usado.
4. Identifique entidade, privilégio, serviço, dono, exposição e atividade atual.
5. Considere explicações legítimas e alternativas maliciosas. Valide por canal independente quando possível.
6. Compare os fatos com critérios organizacionais. Escale se houver risco, urgência, privilégio ou incerteza relevante.
7. Defina próximo passo, responsável e prazo de reavaliação. Se a situação estiver ativa e o dano potencial for alto, considere contenção proporcional em paralelo.

## Fatos, inferências e desconhecidos

| Categoria | Exemplo fictício | Como registrar |
| --- | --- | --- |
| Observado | Registro de autenticação às 01:12 UTC com IP `198.51.100.24`. | Fonte e identificador do registro. O IP pertence a faixa de documentação. |
| Inferido | A origem pode representar viagem ou uso de infraestrutura intermediária. | Hipótese, evidências favoráveis e contrárias, confiança. |
| Desconhecido | Não foi confirmada a identidade da pessoa nem a existência de sessão ativa. | Pergunta, fonte que pode responder, responsável e prazo. |

Um endereço, hash ou nome de ferramenta é indicador para investigação, não prova suficiente de comprometimento. Uma ausência de evento só reduz a hipótese se a fonte tinha cobertura, retenção e coleta adequadas para aquele período.

## Hipóteses concorrentes

Para uma autenticação inesperada, considere: atividade legítima de viagem; VPN ou proxy corporativo; integração ou automação; erro de geolocalização; sessão compartilhada; uso não autorizado. Procure evidências que possam distinguir hipóteses: dispositivo, método e resultado de MFA, aplicação, sessão, mudanças de credencial, privilégio, atividade subsequente e confirmação do titular por canal confiável. Não contate por uma sessão suspeita.

## Perguntas para orientar a análise

- A atividade ainda está acontecendo? Existe sessão ou token ativo?
- A identidade é privilegiada? Que aplicações e dados ela alcança?
- Qual dispositivo e serviço estão envolvidos? Quem é o dono?
- Há mudanças recentes de senha, MFA, grupos ou privilégios?
- Que outras identidades, hosts, sessões ou recursos compartilham indicadores?
- Quais fontes cobrem o período e o que não registram?
- Qual dano pode ocorrer se aguardarmos? Qual dano pode ocorrer se restringirmos agora?
- Que evidência pode desaparecer com a ação e como preservar o necessário?

## Saída da análise inicial

O registro deve conter resumo neutro, fontes, fatos, hipóteses, desconhecidos, impacto potencial, severidade provisória, escopo atual, risco de atividade em andamento, ações já feitas, decisão necessária e próximo passo. Use [registro de decisões](decision-log.md), [timeline](incident-timeline.md) e [handoff](handoff.md) conforme o caso.

---

[← Papéis e responsabilidades](roles-and-responsibilities.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Classificação e severidade →](classification-and-severity.md)
