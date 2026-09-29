# Fundamentos de MITRE ATT&CK

[← Índice do módulo](README.md) · [Página principal](../README.md) · [Táticas →](tactics.md)

## MITRE e ATT&CK

MITRE é a organização de pesquisa e desenvolvimento. ATT&CK é uma de suas bases de conhecimento de segurança cibernética. Dizer “MITRE detectou” ou “o MITRE atacou” confunde a organização com o modelo. Prefira “o ATT&CK descreve”, “a técnica está mapeada no ATT&CK” ou “a MITRE Corporation mantém o projeto”.

ATT&CK expande *Adversarial Tactics, Techniques, and Common Knowledge*. A sigla é secundária ao uso: compartilhar uma descrição de comportamento com identificadores que possam ser pesquisados e versionados.

## Domínios

| Domínio | Escopo geral | Por que importa à defesa |
| --- | --- | --- |
| Enterprise | Sistemas corporativos, identidades, endpoints, redes, nuvem, aplicações e infraestrutura. | Relaciona-se diretamente aos módulos SOC, SIEM, detecção, hunting e resposta deste projeto. |
| Mobile | Dispositivos, sistemas e aplicações móveis. | Há plataformas, capacidades e fontes de telemetria próprias. |
| ICS | Tecnologia operacional, sistemas de controle industrial, ativos e processos industriais. | Disponibilidade, segurança física e efeitos no processo exigem contexto especializado. |

ATT&CK possui matrizes por domínio, mas as matrizes não são universos intercambiáveis. Uma técnica com nome parecido pode ter ID, escopo, relação ou evidência diferente. O exemplo do curso prioriza Enterprise, sem afirmar equivalência automática com Mobile ou ICS.

## Objetivo, comportamento e implementação

Uma **tática** é o objetivo tático associado a uma ação no modelo. Uma **técnica** descreve um comportamento mais geral para atingir objetivo(s). Uma **subtécnica** especializa o comportamento. Uma **procedure** descreve uma instância concreta documentada, vinculada a software, grupo ou campanha por uma relação.

Esses conceitos modelam conhecimento documentado. Eles não descrevem todos os ataques, não garantem que cada adversário siga o mesmo caminho e não revelam por si só o que ocorreu numa organização. A observação local e suas fontes continuam sendo a base de uma conclusão.

## ATT&CK não é uma timeline

A disposição de táticas na matriz organiza navegação, não impõe cronologia. Um adversário pode não usar uma tática, repetir uma técnica, voltar a um objetivo ou realizar atividades simultâneas. Caminhos diferentes podem chegar a resultados semelhantes.

```text
coluna da matriz ≠ ordem cronológica obrigatória
```

ATT&CK também não é uma kill chain universal, um plano de resposta, um catálogo de IOCs ou uma lista de controles. Use cada modelo para a pergunta que ele representa.

## ATT&CK muda

Técnicas, subtécnicas, descrições, relações, plataformas e objetos defensivos evoluem. Objetos podem ser atualizados, depreciados, revogados ou removidos do conjunto corrente. Versões recentes alteraram a estrutura defensiva e as táticas Enterprise. Por isso, uma anotação responsável registra:

```text
ATT&CK ID + domínio + versão + data de análise + evidência
```

Versão e data registram contra qual catálogo o mapping foi feito. Não são promessa de atualização automática nem substituem revisão. Veja [versioning-attack.md](versioning-attack.md).

## Confiança no mapping

High, Medium e Low podem ser uma escala local para expressar confiança no mapping, desde que a legenda defina o que cada valor significa. Não são uma classificação oficial obrigatória do ATT&CK. Diferencie confiança de mapping, severidade do alerta e probabilidade de comprometimento.

Uma hipótese de técnica pode ser útil antes de certeza completa. Rotule-a como hipótese, explique a evidência e os desconhecidos, e atualize ou remova o mapping se novos fatos não o sustentarem.

---

[← Índice do módulo](README.md) · [Página principal](../README.md) · [Táticas →](tactics.md)
