# ATT&CK em Threat Hunting

[← Índice do módulo](README.md) · [Telemetria](attack-to-telemetry.md) · [SOC](attack-for-soc.md) · [Incident Response](attack-for-incident-response.md)

## Matriz como fonte de hipóteses

Use uma técnica para perguntar que comportamento pode ser relevante, que manifestação e que evidência o confirmariam ou refutariam. Uma célula ATT&CK não é hunt pronto. Comece pelo ambiente, fontes disponíveis, risco e lacuna de conhecimento.

```text
Hipótese comportamental
  → população e período em escopo
    → fontes e campos disponíveis
      → consulta exploratória
        → revisão de contexto e hipóteses alternativas
          → resultado, lacuna ou nova pergunta
```

## Perguntas de hunting

- Que ativos e identidades entram na pergunta?
- Que atividade legítima produz eventos semelhantes?
- Que dados poderiam refutar a hipótese?
- Quais fontes estão ausentes ou incompletas?
- O que seria um resultado interessante e qual é o próximo passo?

Registre consultas e períodos, limites de coleta, quantidade de ativos avaliados, observações, resultado negativo e follow-up. Hunting negativo com telemetria incompleta não prova que o comportamento não ocorreu.

## Integração com o módulo 09

O módulo 09 explica planejamento e execução do ciclo de hunting. ATT&CK oferece uma taxonomia e fontes públicas para expandir hipóteses. O hunt deve permanecer ancorado em risco e dados locais, não em percorrer a matriz mecanicamente.
