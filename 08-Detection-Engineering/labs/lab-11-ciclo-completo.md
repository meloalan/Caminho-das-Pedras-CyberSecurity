# Lab 11: Detecção completa e caso composto

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-10-detection-as-code.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../09-Threat-Hunting/README.md)

## Objetivo

Construir uma entrega de engenharia com limites explícitos.

## Cenário

Falhas → sucesso → privilégios de sessão → processo → DNS/rede. Uma criação de conta próxima tem outro ator e host.

## Dados e preparação

Use o dataset do módulo 07, a investigação correspondente e os testes de tuning do módulo 08.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Que vínculos sustentam E01-E08?
2. E09 pertence automaticamente à mesma cadeia?
3. Quais sinais serão obrigatórios ou enriquecimento?
4. Que comportamento, risco e ação justificam a regra?

## Dicas

Sessão usa host e LogonId; processo/rede usa host e ProcessGuid. Proximidade temporal não comprova causalidade.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

A sequência candidata reúne E01/E02/E03 antes de E04. E05 informa privilégios especiais da sessão; E06 compartilha sessão e E07/E08 compartilham execução. Isso sustenta relação observável, não abuso confirmado. E09 no DC por outro ator permanece separado. Defina candidato básico de autenticação e contexto opcional de processo/rede para não perder tudo quando um sensor falta. Declare chaves, tolerância a atraso, campos nulos, risco residual e fila responsável.

</details>

## Especificação comentada para comparar com sua entrega

| Decisão | Proposta fictícia a validar |
| --- | --- |
| 1. Hipótese | Falhas anteriores a um sucesso, na mesma chave, justificam conferir autorização e uso da sessão |
| 2. Risco e telemetria | Uso indevido de credenciais; Security 4625/4624, contexto 4672 e Sysmon 1/3/22 |
| 3. Sinais obrigatórios | Três falhas únicas anteriores ao sucesso, sem exigir sensor Sysmon para criar o candidato |
| 4. Campos | Autoridade, conta, host, IP, LogonType, horário original; sessão e ProcessGuid para enriquecimento |
| 5. Queries | [Correlação](../../07-Buscas-e-Queries-em-SIEM/correlacao-e-joins.md), [sessão](../../07-Buscas-e-Queries-em-SIEM/investigacao.md) e [processo](../../07-Buscas-e-Queries-em-SIEM/pivot.md) |
| 6. Correlação | Falhas em [sucesso-10m, sucesso); mesmo host e sessão para 4672/processo; host + ProcessGuid para DNS/rede |
| 7. Regra candidata | DET-WIN-AUTH-001, experimental; avaliação da condição por sucesso e contexto opcional; configuração do mecanismo depende do produto |
| 8. ATT&CK | Manter hipótese candidata; não marcar brute force específico ou PowerShell abusivo sem evidência que sustente a técnica |
| 9. Severidade | Definir impacto potencial pelo ativo e acesso, sem usar o número de eventos como escala de impacto |
| 10. Confiança | Alta na sequência do fixture, indeterminada na intenção; privilégios e rede acrescentam contexto, não veredito |
| 11. Positivos benignos/FP | Usuário errou senha, serviço desatualizado, administração autorizada, VPN/MFA quando houver dados |
| 12. FN | Atividade lenta, origem variável, falta de IP, fonte ausente ou sucesso não coletado |
| 13. Testes | Identidade, N-1/N/N+1, borda temporal, nulo, duplicata, atraso e entradas fora de ordem |
| 14. Tuning | Comparar 3/5/10, preservar objetivo e criar caso separado se precisar observar falhas sem sucesso |
| 15. Runbook | Validar fonte, conta, autorização, sessão, processo, rede e impacto; escalar com evidência |
| 16. Versão | ID estável, versão inicial, owner LAB, diff e rollback documentados |
| 17. Limites | Fonte de autorização ausente, comandos posteriores incompletos, sem prova de execução em produto |

O código de referência testa a sequência de autenticação. O enriquecimento de sessão/processo/rede é uma etapa de investigação vinculada às queries acima, não um correlacionador composto já implantado. Defina e teste uma janela própria para cada vínculo antes de automatizar essa parte. Não estenda relações entre toda a retenção apenas porque o identificador reaparece.

Na implementação escolhida, defina frequência, lookback e política de atraso; deduplique candidatos por ID estável do sucesso com escopo de fonte/host/canal. Uma sobreposição que recupere dados não deve gerar incidentes novos indefinidamente para o mesmo candidato. Teste também o candidato sem Sysmon: ele deve continuar disponível, com enriquecimento ausente explicitado.

## Implementação e limites

Use [Anatomia de uma detecção operável](../anatomy-of-a-detection.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Especificação, queries vinculadas, regra candidata, ATT&CK justificado, severidade/confiança, FP/FN, matriz, tuning, runbook, versão e lacunas. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Que vínculos sustentam E01-E08?**

<details>
<summary>Ver resposta</summary>

A sequência candidata reúne E01/E02/E03 antes de E04.

</details>

[← Tópico anterior](lab-10-detection-as-code.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../09-Threat-Hunting/README.md)
