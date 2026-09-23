# Como contribuir

[← Voltar para página principal](README.md)

1. Abra uma issue descrevendo a melhoria ou correção e a fonte que a sustenta.
2. Trabalhe em uma branch com uma mudança coerente e textos em português.
3. Use o [template de lab](12-Labs-Praticos/TEMPLATE-LAB.md) ou o [template de detecção](08-Detection-Engineering/TEMPLATE-DETECCAO.md).
4. Diferencie dado sintético, resultado esperado e resultado realmente observado. Não use dumps de provas nem conteúdo copiado sem autorização.
5. Revise nomes, links relativos, hierarquia de títulos e `git diff --check`. Execute `python scripts/validate_docs.py` na raiz.
6. Remova identificadores pessoais, nomes de tenant, IPs reais e segredos das evidências publicáveis. Revise também imagens e histórico: `.gitignore` não detecta segredos dentro de documentos nem protege arquivos já rastreados.
7. Envie pull request com motivo, arquivos alterados e testes executados. Declare o que depende de validação externa.

## Relato de exposição acidental

Não abra issue pública com a credencial. Revogue/rotacione primeiro e comunique o responsável por canal privado. Remoção do arquivo no último commit não remove versões anteriores.

## Critérios editoriais

Uma página deve ensinar um conceito, propor uma prática e definir uma entrega verificável. Uma query precisa declarar tabela, intenção, funcionamento, falsos positivos e melhoria possível. Contribuições seguem a [licença MIT](LICENSE).
