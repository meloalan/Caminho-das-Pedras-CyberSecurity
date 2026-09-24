# Laboratórios de SIEM na Prática

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](../microsoft-sentinel.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-01-entendendo-o-pipeline.md)

## Escolha um percurso

**Offline:** leia o dataset fictício, descreva consultas e calcule resultados esperados com o script local. **Uma plataforma:** execute na tecnologia disponível, documentando o schema. **Comparação:** traduza a intenção para as outras sem afirmar execução que não ocorreu. Os percursos ensinam as mesmas perguntas, com evidências diferentes.

Não é necessário instalar quatro SIEMs nem contratar cloud. A configuração pequena de [Wazuh](../wazuh.md), [Splunk](../splunk.md), [QRadar](../qradar.md) e [Sentinel](../microsoft-sentinel.md) está nas respectivas páginas. Escolha apenas uma quando houver ambiente e autorização.

## Preparação e segurança

Use VM própria, rede de laboratório e dados sintéticos. Não execute geração de eventos ou mudanças de auditoria em máquinas corporativas. Não desabilite controles para facilitar a coleta. Nenhum exercício exige ataque, password spray, exploração, bloqueio de conta ou contenção real.

Registre versão, fonte, campos, janela e resultado. Logs reais podem conter dados pessoais/segredos e devem permanecer no local autorizado. O repositório recebe apenas notas e exemplos fictícios.

## Sequência e entregas

| Lab | Entrega | Dependência |
| --- | --- | --- |
| [01: Entendendo o pipeline](lab-01-entendendo-o-pipeline.md) | Contrato e comparação origem/destino | Nenhuma |
| [02: Primeiras consultas](lab-02-primeiras-consultas.md) | Consultas e amostra conferida | Lab 01 |
| [03: Autenticação Windows](lab-03-windows-authentication.md) | Chaves, hipóteses e volume | Lab 02 |
| [04: Criação de usuário](lab-04-user-creation.md) | Ator/alvo e contexto da criação | Lab 02 |
| [05: Criação de processo com Sysmon](lab-05-sysmon-process-creation.md) | Árvore e limites da telemetria | Lab 02 |
| [06: Da query à regra](lab-06-detection-rule.md) | Especificação e matriz de testes | Labs 03 e 04 |
| [07: Tuning com regressão](lab-07-tuning.md) | Versão antes/depois e perdas | Lab 06 |
| [08: Investigação do cenário final](lab-08-investigation.md) | Timeline e relatório proporcional | Labs 03 a 05 |
| [09: Threat hunting e raridade](lab-09-threat-hunting.md) | Hipótese, pivô e melhoria | Lab 08 |

## Dataset e conferência offline

O [cenario-final.jsonl](dados/cenario-final.jsonl) contém dez observações fictícias de 2026-09-20 UTC. É um modelo didático com campos comuns, não um export nativo. Não ingira esse JSON numa tabela SecurityEvent nem finja que ele é um EVTX. Para ingestão de laboratório, seria necessário um índice/tabela customizada e outro contrato de consulta.

O [script de análise](dados/analisar_cenario.py) usa apenas a biblioteca padrão Python, lê o arquivo local e imprime contagens, sequência candidata e timeline. Não acessa rede nem modifica o dataset. Execute a partir desta pasta:

```powershell
python .\dados\analisar_cenario.py
```

Resultado esperado: dez registros, cinco falhas 4625, um sucesso 4624 e uma sequência candidata com três falhas da chave compatível antes do sucesso. Uma falha homônima em outra autoridade e outra conta de serviço devem ficar fora dessa sequência. Isso testa raciocínio sobre o dataset; não comprova execução SPL, AQL, KQL ou Wazuh.

## Modelo de evidência de cada lab

```text
Percurso: offline / produto e versão
Objetivo e pergunta:
Fontes, campos e janela:
Configuração ou consulta usada:
Resultado esperado:
Resultado obtido e referência:
Diferenças e explicação:
Limitações e próximo passo:
```

Os roteiros não vêm preenchidos como se tivessem sido executados no seu ambiente. Os resultados offline podem ser reproduzidos; a configuração dos produtos permanece a validar por quem fizer o lab. O checklist individual fica na [Issue de progresso](https://github.com/meloalan/Caminho-das-Pedras-CyberSecurity/issues/new?template=modulo-06-siem-na-pratica.md).

## Checkpoint

**O JSON é um export nativo do Windows?**

<details>
<summary>Ver resposta</summary>

Não. É uma representação didática sintética. As consultas de produto exigem seu próprio schema.

</details>

**Preciso instalar todos os SIEMs?**

<details>
<summary>Ver resposta</summary>

Não. Faça offline ou em uma plataforma e compare as intenções nas demais.

</details>

[← Tópico anterior](../microsoft-sentinel.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-01-entendendo-o-pipeline.md)
