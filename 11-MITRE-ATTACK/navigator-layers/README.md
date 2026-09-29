# Layers de exemplo

[← Índice do módulo](../README.md) · [Como usar Navigator](../attack-navigator.md) · [Avaliação de cobertura](../detection-coverage.md) · [Página principal](../../README.md)

## Escopo

Os JSON deste diretório são exemplos educacionais sintéticos para ATT&CK Enterprise 19.2, Navigator 5.3.2 e layer format 4.5. Não descrevem o ambiente do leitor nem resultados reais de detecção. IDs externos foram selecionados como exemplos atuais. Confirme-os antes de adaptar.

## Arquivos

- `coverage-example.json`: ilustra estado hipotético de uma manifestação estreita e uma validação ainda pendente.
- `hunt-example.json`: destaca hipóteses de hunting, não presença confirmada de ameaça.
- `incident-example.json`: representa hipóteses comportamentais fictícias numa investigação didática, sem atribuição.

## Convenção local de cores

Verde significa exemplo de detecção validada dentro de um escopo explicitado. Amarelo significa telemetria candidata ainda não validada. Vermelho significa lacuna conhecida no escopo fictício. Cinza significa fora do escopo. Esta legenda é local, não oficial. Cada usuário deve adaptá-la e documentar critérios, ativos, fonte, versão e evidência no template de Coverage Assessment.

Abra uma layer no [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/), inspecione `description`, legenda, comentários e versão. Não interprete a cor como cobertura integral da técnica, prova de comprometimento ou indicador de risco sem contexto.
