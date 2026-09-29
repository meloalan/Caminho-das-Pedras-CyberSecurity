# ATT&CK em Detection Engineering

[← Índice do módulo](README.md) · [Mapeamento](detection-mapping.md) · [Detection Strategies](detection-strategies.md) · [Cobertura](detection-coverage.md)

## Do requisito comportamental ao teste

Detection Engineering usa ATT&CK para organizar comportamento de interesse, comparar lógica e registrar lacunas. O trabalho de engenharia transforma uma hipótese em implementação testável; o ID é metadado e contexto, não especificação completa da regra.

1. Escolha manifestação observável e escopo de plataforma.
2. Consulte técnica, subtécnica e Detection Strategy atuais.
3. Identifique Analytics e Data Components relevantes.
4. Mapeie cada requisito de dado à fonte e aos campos locais.
5. Escreva lógica independente de fabricante antes de escolher sintaxe de SIEM quando possível.
6. Teste positivos, negativos, casos de fronteira e tolerância a campos ausentes.
7. Registre falsos positivos, evasões previsíveis e restrições.
8. Versione a regra, o mapping e a validação em conjunto.

## Regra de qualidade

Uma consulta que detecta um conjunto limitado de eventos deve documentar esse conjunto. Se os dados não permitem diferenciar pai e subtécnica, reduza a especificidade da tag ou justifique a inferência. Não declare cobertura geral por detecção de uma assinatura estreita.

## Independência de SIEM

ATT&CK não depende de Sentinel, Splunk, QRadar, Wazuh ou outra plataforma. Produtos podem mudar a sintaxe, ingestão e esquema; comportamento e critérios de evidência continuam sendo descritos separadamente. Guarde consulta específica como implementação ligada a fontes, campos e versão do produto.

## Integração com o módulo 08

O módulo 08 trata ciclo de vida, engenharia, teste e manutenção de detecções. Este módulo conecta o comportamento ao vocabulário ATT&CK vigente, estratégias públicas e Data Components, sem duplicar o processo geral de construção de regra.
