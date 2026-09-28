# Detecções como artefatos de estudo

[Página principal](../README.md) · [Módulo 08](../08-Detection-Engineering/README.md)

Especificações, regras experimentais e testes sobre dados fictícios. Nenhum arquivo foi implantado automaticamente em SIEM. Queries de investigação continuam no [catálogo por caso de uso](../queries/README.md).

## Artefatos

| Arquivo | Tipo e papel |
| --- | --- |
| [DET-WIN-ACCOUNT-001.yml](windows/account-management/DET-WIN-ACCOUNT-001.yml) | Especificação educacional própria, não Sigma nem padrão de mercado |
| [wazuh-account-created.xml](windows/account-management/wazuh-account-created.xml) | Implementação didática no contrato Windows EventChannel; validar com logtest |
| [office-powershell.sigma.yml](windows/process-creation/office-powershell.sigma.yml) | Sigma experimental para cadeia de processo, sem veredito de malware |
| [Baseline Sigma anterior](../queries/sigma/windows-account-created.yml) | Mantida no caminho original, sem duplicar o artefato |
| [evaluate.py](tools/evaluate.py) | Lógica de referência Python para seleção, correlação e tuning |
| [test_detection_logic.py](tests/test_detection_logic.py) | Casos de unidade e regressão |
| [validate_artifacts.py](tools/validate_artifacts.py) | Parsing local de YAML, Sigma, XML e JSON |

## Contrato dos fixtures

[account-cases.json](tests/account-cases.json) usa event_id inteiro, provider/channel textuais e campos didáticos host, timestamp, actor/actor_domain e user/domain. Os timestamps são UTC com fuso. Esses nomes não são campos universais dos SIEMs. Um ator ausente gera aviso de contexto, sem apagar a correspondência 4720.

[tuning.jsonl](tests/tuning.jsonl) tem cem candidatos 4720 fictícios em 28/09/2026. T001-T060 são provisionamento aprovado por svc_provision.lab; T061-T070 usam svc_backup.lab e exigem investigação no rótulo do exercício; T071-T090 também são positivos; T091-T100 são negativos. A classificação requires_investigation é ground truth artificial e não entra na lógica de seleção/exceção. approved_change representa contexto já conferido num registro independente fictício, não uma autorização autodeclarada pelo evento.

Uma linha equivale a um candidato e, no experimento, a um alerta não agrupado. Baseline: 100 alertas. Exceção ampla: 30, perdendo dez positivos. Exceção restrita: 40, preservando os 30 positivos deste conjunto. Isso não comprova cobertura fora do fixture.

[process-cases.json](tests/process-cases.json) usa Image e ParentImage normalizados para demonstrar a condição Sigma. P01 tem pai Office; P02 tem pai Explorer; P03 tem pai nulo. Correspondência esperada não significa atividade maliciosa. A matriz não executa um backend Sigma.

A correlação reutiliza o [dataset do módulo 07](../07-Buscas-e-Queries-em-SIEM/labs/dados/README.md). Chave: autoridade, usuário, host, IP e LogonType. Janela de falhas: [sucesso-10m, sucesso). ID do fixture é único; em dados reais a identidade do registro deve incluir o escopo da fonte. Duplicatas conflitantes são erros de qualidade.

## Executar localmente

Na raiz, os testes comportamentais usam biblioteca padrão Python:

```sh
python -B -m unittest discover -s detections/tests -v
python detections/tools/evaluate.py
```

Para validar também a estrutura Sigma e YAML, use um ambiente de desenvolvimento:

```sh
python -m pip install -r detections/requirements-validation.txt
python detections/tools/validate_artifacts.py
```

Parsing e lógica Python não substituem query, CRE, scheduler, parser real ou wazuh-logtest. Registre versão, saída esperada/obtida e pendências no [template de detecção](../08-Detection-Engineering/TEMPLATE-DETECCAO.md).
