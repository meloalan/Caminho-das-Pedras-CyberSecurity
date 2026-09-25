# Visuais da página inicial

[Página principal](../../../README.md)

Ilustrações originais produzidas por código para apresentar a trilha e o raciocínio investigativo. Não representam uma sessão real de SIEM nem evidências de laboratório.

| Arquivo | Uso | Dimensões |
| --- | --- | --- |
| banner-caminho.gif | Capa com progressão entre base, dados, investigação e critério | 1600 × 520 |
| fluxo-investigacao.gif | Pergunta, dados, consulta e evidência, com retorno aos dados | 1200 × 580 |
| banner-caminho.png | Capa estática completa | 1600 × 520 |
| fluxo-investigacao.png | Fluxo estático completo | 1200 × 580 |

Os GIFs executam um ciclo de 4,6 segundos e param no desenho completo. O texto permanece visível em todos os quadros; movimento não é necessário para entender o conteúdo. O README inclui descrições e links para as alternativas estáticas. Não há serviço externo de animação.

## Gerar novamente

Requer Python, Pillow e uma fonte instalada: Segoe UI no Windows ou DejaVu Sans no Linux. Para instalar a dependência em seu ambiente de desenvolvimento:

```sh
python -m pip install Pillow
python scripts/render_home_visuals.py
```

Execute na raiz do repositório. O [gerador](../../../scripts/render_home_visuals.py) verifica dimensões do texto, duração e presença de múltiplos quadros. Confira também os arquivos visualmente antes de publicar. Fontes diferentes podem mudar o desenho final.

O GitHub aceita GIF; seu visualizador de SVG tem restrições de animação, conforme a [documentação de arquivos não textuais](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files).
