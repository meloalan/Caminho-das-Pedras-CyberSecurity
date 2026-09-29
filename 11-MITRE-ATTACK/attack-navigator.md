# ATT&CK Navigator

[← Índice do módulo](README.md) · [Camadas de exemplo](navigator-layers/README.md) · [Cobertura](detection-coverage.md)

## Visualizar uma avaliação

ATT&CK Navigator permite visualizar layers associadas a uma matriz ATT&CK. Uma layer é um artefato analítico editável, não uma certificação de cobertura. Ela é útil para comunicar escopo e hipóteses quando sua legenda e proveniência são explícitas.

Use o [Navigator oficial](https://mitre-attack.github.io/attack-navigator/) e a [especificação atual de layer](https://github.com/mitre-attack/attack-navigator/blob/master/layers/spec/v4.5/layerformat.md) para entender o formato. Este material foi conferido para Navigator 5.3.2 e layer format 4.5.

## Convenção didática deste repositório

| Cor | Significado local |
| --- | --- |
| Verde | Exemplo de detecção validada para a manifestação e escopo registrados. |
| Amarelo | Há telemetria candidata, mas não há teste suficiente para afirmar eficácia. |
| Vermelho | Exemplo de lacuna conhecida no escopo declarado. |
| Cinza | Fora do escopo desta avaliação didática. |

As cores são convenção local, não semântica oficial de ATT&CK. Layers neste módulo são ilustrações fictícias. Nenhuma cor declara o estado real da organização.

## Ler e editar uma layer

1. Abra uma layer local no Navigator ou carregue-a conforme a interface vigente.
2. Confira domain, attack version e layer version.
3. Leia `legendItems`, `description`, `comments` e os metadados de cada técnica.
4. Inspecione uma técnica colorida e anote o critério da cor.
5. Modifique a cópia para representar um escopo real e documentado.
6. Exporte a layer e valide JSON e IDs contra o bundle utilizado.

## Limites

Uma célula colorida não confirma fonte implantada, campos íntegros, qualidade da regra, teste em ativos ou capacidade de responder ao alerta. Guarde a avaliação completa e sua evidência junto à layer. Reveja mappings após atualizações ATT&CK. Consulte [camadas de exemplo](navigator-layers/README.md) e o template de [coverage assessment](TEMPLATE-COVERAGE-ASSESSMENT.md).
