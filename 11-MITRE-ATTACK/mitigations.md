# Mitigações

[← Índice do módulo](README.md) · [Modelo de dados](attack-data-model.md) · [Incident Response](attack-for-incident-response.md)

## Reduzir risco é diferente de detectar

ATT&CK registra objetos Mitigation associados a técnicas. Mitigação descreve uma possibilidade para prevenir, dificultar ou limitar um comportamento. Ela não é um alerta, uma evidência nem uma garantia de que o risco foi removido.

Ao avaliar uma mitigação, confirme aplicabilidade, pré-requisitos, efeito colateral, responsável, ativos cobertos e método para verificar implantação. Uma política pode existir sem estar aplicada em todos os sistemas. Uma mitigação pode reduzir uma rota e ainda deixar outras manifestações possíveis.

Consulte [Mitigations](https://attack.mitre.org/mitigations/) e as relações na página da técnica. Trate recomendações como ponto de partida e valide-as com os responsáveis técnicos do ambiente.

## Exemplo de raciocínio

Para reduzir risco associado a uso indevido de interpretadores, controles de aplicação, privilégios mínimos, logging adequado e restrições de execução podem ser considerados de acordo com a plataforma. Cada um tem objetivos e impactos diferentes. Nenhum deles prova que toda execução suspeita será detectada.

## Resposta a lacunas

Uma avaliação pode indicar Telemetry Gap, Detection Gap ou controle preventivo ausente. Compare ações de mitigação, instrumentação, detecção e resposta pelo risco e esforço. Registre quem valida resultado e quando. Evite converter cada técnica da matriz em uma lista mandatória de controles.
