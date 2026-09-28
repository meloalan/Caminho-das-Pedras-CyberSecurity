# Engenharia de detecção: da demanda à operação

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](README.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-hypothesis.md)

## A disciplina

Detection Engineering transforma riscos e comportamentos relevantes em sinais que uma equipe consegue investigar, testar e manter. O trabalho inclui escolher o que observar, provar que a fonte chega, desenvolver lógica, definir resposta e acompanhar a detecção depois da publicação. A query é um componente dessa entrega.

Uma demanda como “detectar criação suspeita de contas” ainda não é uma especificação. Falta definir autoridade da conta, ativos, administradores esperados, impacto e o que torna a investigação útil. Um 4720 confirma criação sob condições de auditoria; a classificação da intenção exige contexto adicional.

## Objetos diferentes

| Objeto | O que representa | O que não garante |
| --- | --- | --- |
| Log | Registro produzido por uma fonte | Completude ou intenção do ator |
| Query | Seleção ou transformação de dados | Execução recorrente e resposta |
| Detecção | Capacidade especificada de reconhecer um comportamento observável | Implantação em todos os ativos |
| Regra | Implementação de condições e ações em um mecanismo | Equivalência entre produtos |
| Alerta | Sinal gerado para avaliação | Incidente confirmado |
| Incidente | Ocorrência tratada segundo critérios da organização | Que qualquer alerta isolado seja suficiente |

Log ≠ query ≠ detecção ≠ regra ≠ alerta ≠ incidente. Vários alertas podem contribuir para uma investigação; agrupamento e nomenclatura variam entre produtos e organizações. Uma investigação pode terminar com atividade autorizada ou evidência insuficiente.

## Relação com outras disciplinas

| Entrada ou parceria | Como contribui | Limite |
| --- | --- | --- |
| Threat modeling | Prioriza risco e ativos | Um risco pode não ser observável pela fonte atual |
| Threat Intelligence | Sugere indicadores e comportamentos relevantes | Feed não é autorização para criar milhares de alertas |
| Threat Hunting | Testa hipóteses e encontra padrões | Nem todo achado é repetível ou acionável |
| SOC e Incident Response | Informam contexto, decisões e lacunas | Triagem também pode estar incompleta |
| Purple Team | Confere observabilidade em exercício autorizado | Resultado vale para o cenário e ambiente testados |
| SIEM, EDR e XDR | Implementam coleta, análise e resposta | Cada mecanismo tem restrições e contratos |
| MITRE ATT&CK | Descreve comportamento e referências defensivas | Tag não mede cobertura |

Essas relações são um modelo de estudo. Equipes reais distribuem responsabilidades de maneiras diferentes.

## Primeiro contrato

Antes de abrir o editor, escreva: “Em quais ativos, qual atividade, observada por quais fontes, deve produzir qual ação de investigação?” Para conta criada, a ação inicial pode ser conferir ator, alvo, autorização e mudanças posteriores. Bloquear toda conta recém-criada seria uma resposta desproporcional ao sinal.

Preservamos a base do módulo anterior: comportamento observável, telemetria, lógica acionável, severidade distinta de confiança e responsável definido. O [template](TEMPLATE-DETECCAO.md) agora transforma esses conceitos em campos de trabalho.

A operação do [SOC](../05-SOC-Blue-Team/README.md), o [pipeline SIEM](../06-SIEM-na-Pratica/README.md) e a [linguagem de consulta](../07-Buscas-e-Queries-em-SIEM/README.md) são pré-requisitos. Aqui estudamos como tornar essa capacidade confiável e operável.

## Checkpoint

**Uma query correta basta para promover a regra?**

<details>
<summary>Ver resposta</summary>

Não. Faltam cobertura, testes do agendamento, contexto, volume, runbook, responsável, monitoramento e plano de reversão.

</details>

[← Tópico anterior](README.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-hypothesis.md)
