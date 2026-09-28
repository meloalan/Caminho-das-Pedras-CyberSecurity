# Quem monitora as detecções?

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](coverage.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-metrics.md)

## Silêncio não é ausência de ameaça

Zero alertas pode significar comportamento ausente, filtro novo, fonte parada, campo perdido, permissão alterada ou regra quebrada. A saúde precisa combinar evidência de execução com saúde da fonte e qualidade dos dados.

| Sinal | Verificação | Encaminhamento |
| --- | --- | --- |
| Regra não executou | Scheduler, erro, timeout e permissões | Owner da detecção/plataforma |
| Fonte silenciosa | Último evento, heartbeat e inventário | Equipe de coleta |
| Campo desapareceu | Taxa de nulos e amostra original | Parser/normalização |
| Atraso aumentou | Diferença entre geração e ingestão | Transporte e dimensionamento |
| Alertas caíram a zero | Volume da fonte + diff da regra + janela | Revisão conjunta |
| Alertas explodiram | Mudança de atividade, duplicação ou lógica | SOC e engenharia |
| Query ficou lenta | Duração, recursos e população | Otimização sem perder escopo |

## Teste de continuidade

Defina uma observação de saúde independente da própria condição suspeita: chegada de dados esperados, execução registrada e presença dos campos. Uma regra que só monitora 4720 não é um heartbeat confiável de um host que raramente cria contas.

Um teste sintético controlado pode validar o caminho em laboratório, mas deve ser identificado para não induzir resposta real. Documente quem acompanha a falha e como a capacidade fica marcada enquanto está indisponível.

## Implementação depende da plataforma

Sentinel oferece recursos de saúde de analytics; Splunk possui histórico de execução e scheduler; QRadar requer observar processamento, fonte e regra; Wazuh precisa de observação de agentes, análise e entrega ao indexer. Os nomes e APIs variam. Consulte as [referências](referencias.md) e registre qual sinal foi usado no seu ambiente.

## Revisão após mudança

Parser, agente, schema, produto e inventário podem mudar sem alteração no arquivo da regra. Associe revisão a mudanças relevantes e a uma cadência baseada no risco. Não há periodicidade universal neste material. Uma exceção expirada é um motivo próprio de revisão.

**Cenário:** ontem havia dez alertas e hoje nenhum. Antes de comemorar, compare eventos totais, último recebimento, campos obrigatórios e execução. Se a fonte parou, o status correto é capacidade degradada, não “ambiente limpo”.

## Checkpoint

**Uma query que executa sem erro está necessariamente saudável?**

<details>
<summary>Ver resposta</summary>

Não. Ela pode selecionar um campo vazio, fonte incompleta ou população errada. Sucesso de execução e qualidade de dados são controles distintos.

</details>

[← Tópico anterior](coverage.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-metrics.md)
