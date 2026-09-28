# 08 Detection Engineering

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](../07-Buscas-e-Queries-em-SIEM/README.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](fundamentos.md)

> Se uma query retorna resultados, isso significa que temos uma boa detecção?

Não. Ainda precisamos definir comportamento, risco, dados, cobertura, atividades legítimas semelhantes, testes, reação do SOC, volume, custo e manutenção.

![Módulo 08: hipótese, telemetria, lógica, teste e operação](../assets/images/banners/banner-08-detection-engineering.png)

> Uma query encontra dados. Uma detecção transforma evidência observável em um sinal operacional que pode ser testado, mantido e melhorado.

## O que é Detection Engineering?

É a disciplina de transformar risco e comportamento relevante em capacidade observável, testada e operável. Uma detecção é um produto de segurança: tem hipótese, dependências, lógica, owner, resposta, saúde e critério de aposentadoria. Ela precisa continuar útil quando o ambiente muda.

## Detecção não é sinônimo de query

**Log ≠ query ≠ detecção ≠ regra ≠ alerta ≠ incidente.** Uma query pode responder uma pergunta, apoiar hunting ou compor uma regra. A regra pode gerar alerta. O alerta pode iniciar investigação, que pode terminar sem incidente confirmado. Modelos de agrupamento variam entre plataformas.

![Dos registros à decisão: cada etapa tem uma responsabilidade](../assets/images/08-detection-engineering/objetos.svg)

## Ciclo contínuo

O trabalho volta a etapas anteriores: tuning altera lógica, investigação revela fonte faltante, teste encontra campo errado, produção muda e um falso negativo exige revisar a hipótese.

<details>
<summary>Ver o ciclo completo em Mermaid animado</summary>

```mermaid
flowchart TD
    N0["Risco"] e0@--> N1["Comportamento"]
    N1["Comportamento"] e1@--> N2["Hipótese"]
    N2["Hipótese"] e2@--> N3["Telemetria"]
    N3["Telemetria"] e3@--> N4["Campos"]
    N4["Campos"] e4@--> N5["Lógica"]
    N5["Lógica"] e5@--> N6["Query"]
    N6["Query"] e6@--> N7["Teste"]
    N7["Teste"] e7@--> N8["Detecção"]
    N8["Detecção"] e8@--> N9["Alerta"]
    N9["Alerta"] e9@--> N10["Triagem e investigação"]
    N10["Triagem e investigação"] e10@--> N11["Feedback"]
    N11["Feedback"] e11@--> N12["Tuning"]
    N12["Tuning"] e12@--> N13["Validação"]
    N13["Validação"] e13@--> N14["Versionamento"]
    N14["Versionamento"] e14@--> N15["Manutenção"]
    e0@{ animation: slow }
    e1@{ animation: slow }
    e2@{ animation: slow }
    e3@{ animation: slow }
    e4@{ animation: slow }
    e5@{ animation: slow }
    e6@{ animation: slow }
    e7@{ animation: slow }
    e8@{ animation: slow }
    e9@{ animation: slow }
    e10@{ animation: slow }
    e11@{ animation: slow }
    e12@{ animation: slow }
    e13@{ animation: slow }
    e14@{ animation: slow }
    N12 b0@-- "nova lógica" --> N5
    b0@{ animation: slow }
    N10 b1@-- "telemetria faltante" --> N3
    b1@{ animation: slow }
    N7 b2@-- "campo incorreto" --> N4
    b2@{ animation: slow }
    N15 b3@-- "mudança ou falso negativo" --> N2
    b3@{ animation: slow }
```

</details>

![Ciclo de engenharia com retorno por testes e feedback](../assets/images/08-detection-engineering/ciclo.svg)

## Da hipótese ao alerta

Começar com “4625 = High” pula a decisão principal. Comece com um padrão de autenticação que mereça investigação; examine conta, autoridade, host, origem, tipo, janela, baseline e contexto de VPN/MFA quando houver essas fontes. Só depois escolha query, regra e ação.

```mermaid
flowchart TD
    N0["Hipótese testável"] e0@--> N1["Telemetria e campos"]
    N1["Telemetria e campos"] e1@--> N2["Lógica implementável"]
    N2["Lógica implementável"] e2@--> N3["Teste e validação"]
    N3["Teste e validação"] e3@--> N4["Sinal para o SOC"]
    N4["Sinal para o SOC"] e4@--> N5["Contexto e decisão"]
    e0@{ animation: slow }
    e1@{ animation: slow }
    e2@{ animation: slow }
    e3@{ animation: slow }
    e4@{ animation: slow }
    N3 b0@-- "lacuna" --> N1
    b0@{ animation: slow }
    N5 b1@-- "feedback" --> N0
    b1@{ animation: slow }
```

## Como este módulo se conecta

| Módulo | Papel |
| --- | --- |
| [05: SOC e Blue Team](../05-SOC-Blue-Team/README.md) | Operação, triagem e decisão |
| [06: SIEM na Prática](../06-SIEM-na-Pratica/README.md) | Coleta, parser, normalização e arquitetura |
| [07: Buscas e Queries](../07-Buscas-e-Queries-em-SIEM/README.md) | Filtros, agregações, tempo e correlação |
| 08: Detection Engineering | Transformar dados e queries em detecções confiáveis e operáveis |

## O que você aprenderá

| Etapa | Conteúdo | Entrega |
| --- | --- | --- |
| Projetar | Hipótese, ciclo de vida, telemetria e tipos | Contrato e lacunas |
| Implementar | Casos, anatomia, severidade e multisiem | Regra candidata e alerta contextualizado |
| Validar | Positivos, negativos, bordas, atraso e Sigma | Matriz reproduzível |
| Melhorar | Tuning, exceções, FP/FN e métricas | Comparação com perdas explícitas |
| Operar | Runbook, saúde, cobertura e review | Responsabilidade e observabilidade |
| Manter | Versionamento, feedback e aposentadoria | Histórico e transição controlada |

## Uma detecção em quatro plataformas

A baseline de conta Windows criada mantém hipótese e telemetria comuns. [A implementação](multisiem-detection.md) usa Analytics Rule/KQL, saved search/alert/SPL conforme o produto Splunk, CRE no QRadar e regra no servidor Wazuh. AQL e pesquisa no indexer apoiam investigação, mas não são equivalentes ao motor de regras. Nenhum exemplo depende exclusivamente de Sentinel.

## Percurso completo

- [Engenharia de detecção: da demanda à operação](fundamentos.md)
- [Hipóteses que podem ser testadas](detection-hypothesis.md)
- [Ciclo de vida: desenvolver, operar e aposentar](detection-lifecycle.md)
- [Telemetria: contrato, cobertura e lacunas](telemetry-requirements.md)
- [Tipos de lógica e evolução do sinal](detection-types.md)
- [Cinco casos de uso: do sinal à decisão](casos-de-uso.md)
- [Anatomia de uma detecção operável](anatomy-of-a-detection.md)
- [Severidade, confiança e prioridade](severity-and-confidence.md)
- [Classificar resultados sem esconder falsos negativos](false-positives.md)
- [Tuning: reduzir custo preservando o que importa](tuning.md)
- [Validar a capacidade, não só a sintaxe](detection-validation.md)
- [Testes reproduzíveis com dados fictícios](testing-detections.md)
- [Uma especificação de conta criada, quatro implementações](multisiem-detection.md)
- [Sigma: descrição portável, validação específica](sigma.md)
- [Detection as Code: mudança com evidência e reversão](detection-as-code.md)
- [ATT&CK com evidência e escopo](mitre-mapping.md)
- [Cobertura real e dívida de detecção](coverage.md)
- [Quem monitora as detecções?](detection-health.md)
- [Métricas com população e denominador](detection-metrics.md)
- [Do alerta à decisão: runbook de triagem](runbooks.md)
- [Hunting, incidentes e inteligência como entradas](feedback-to-detections.md)
- [Versão, owner e histórico de mudança](versioning.md)
- [Aposentar sem perder rastreabilidade](retiring-detections.md)
- [Doze erros que deterioram uma detecção](anti-patterns.md)
- [Template profissional de detecção](TEMPLATE-DETECCAO.md)
- [Referências e matriz de eventos](referencias.md)

## Laboratórios e portfólio

[Onze labs](labs/README.md) levam da hipótese sem código ao caso final com autenticação, sessão, processo e rede. Incluem um experimento em que 100 → 30 alertas esconde dez casos relevantes e uma alternativa de 40 preserva os positivos do fixture.

Entregas: especificação, Sigma, matriz de testes, relatório de tuning, matriz de cobertura e histórico versionado. O [catálogo detections](../detections/README.md) reúne arquivos executáveis e contratos; as queries detalhadas continuam no módulo 07.

## Checklist de progresso

Abra o [template de progresso](../.github/ISSUE_TEMPLATE/modulo-08-detection-engineering.md) para acompanhar 21 itens. Todos começam desmarcados. Marque apenas o que você efetivamente estudou, executou e registrou.

## Limites dos resultados

Dados são fictícios. Testes locais e parsing de YAML/Sigma/XML não provam execução em SIEM. A integração depende de produto, versão, coleta, campos, agendamento e fila. Nenhum sinal isolado confirma ataque; nenhuma automação de bloqueio é implantada aqui.

## Checkpoint

**Qual é a primeira decisão depois de uma query retornar dados?**

<details>
<summary>Ver resposta</summary>

Conferir se a população e os campos sustentam o comportamento de interesse. Depois avaliar teste, contexto, ação, custo e operação antes de chamar o resultado de detecção pronta.

</details>

[← Tópico anterior](../07-Buscas-e-Queries-em-SIEM/README.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](fundamentos.md)
