"""Verifica links Markdown locais e estrutura básica; não executa KQL ou labs."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_LAB = [
    'Objetivo', 'Cenário', 'Arquitetura', 'Pré-requisitos',
    'Ferramentas utilizadas', 'Execução', 'Logs gerados', 'Evidências',
    'Investigação', 'Query', 'Regra de detecção', 'MITRE ATT&CK',
    'Resultado esperado', 'Resultado obtido', 'O que aprendi',
    'Possíveis melhorias', 'Próximos passos',
]
errors = []
checked = 0
documents = sorted(ROOT.rglob('*.md'))
for path in documents:
    relative = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding='utf-8')
    if '\ufffd' in text:
        errors.append(f'{relative}: caractere de substituição Unicode')
    if not text.startswith('# '):
        errors.append(f'{relative}: falta título H1 inicial')
    if len(re.findall(r'^# ', text, re.M)) != 1:
        errors.append(f'{relative}: esperado exatamente um H1')
    if len(re.findall(r'^```', text, re.M)) % 2:
        errors.append(f'{relative}: bloco de código não fechado')
    prose = re.sub(r'^```.*?^```[^\n]*', '', text, flags=re.M | re.S)
    last_level = 0
    for match in re.finditer(r'^(#{1,6}) ', prose, re.M):
        level = len(match[1])
        if level > last_level + 1:
            errors.append(f'{relative}: salto na hierarquia de títulos')
        last_level = level
    if path.name == 'README.md' and path != ROOT / 'README.md':
        if 'Página principal' not in text and 'página principal' not in text:
            errors.append(f'{relative}: falta navegação para a página principal')
    for link in re.findall(r'\]\(([^\s)]+)\)', prose):
        parts = urlsplit(link)
        if parts.scheme or link.startswith('#'):
            continue
        checked += 1
        target = (path.parent / unquote(parts.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f'{relative}: link local inválido: {link}')
        elif parts.fragment:
            errors.append(f'{relative}: fragmento requer revisão manual: {link}')
    if re.match(r'12-Labs-Praticos/\d[^/]+/README.md', relative):
        for heading in REQUIRED_LAB:
            if f'## {heading}\n' not in text:
                errors.append(f'{relative}: falta seção {heading}')
        if 'TODO: adicionar evidência real do laboratório' not in text:
            errors.append(f'{relative}: falta marcação de evidência pendente')

for query in (ROOT / 'queries/kql').glob('*.kql'):
    doc = query.with_suffix('.md')
    if not doc.exists() or query.read_text(encoding='utf-8').strip() not in doc.read_text(encoding='utf-8'):
        errors.append(f'{query.name}: query e documentação divergentes')

for error in errors:
    print('ERRO:', error)
print(f'{len(documents)} documentos; {checked} links locais; {len(errors)} erros.')
sys.exit(bool(errors))
