from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path('_site')
errors = []
class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name not in ('href', 'src') or not value: continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path: continue
            target = root / unquote(url.path).lstrip('/') if url.path.startswith('/') else self.page.parent / unquote(url.path)
            if target.is_dir(): target = target / 'index.html'
            if not target.exists(): errors.append(f'{self.page}: missing {value}')
for page in root.rglob('*.html'):
    parser = Links(); parser.page = page; parser.feed(page.read_text())
for expected in ('index.html', 'research/index.html', 'cv/index.html', '404.html', 'assets/css/main.css', 'assets/img/portrait.jpg', 'assets/pdf/yonggang-li-cv.pdf'):
    if not (root/expected).exists(): errors.append(f'Missing output: {expected}')
for page in (root/'index.html', root/'research/index.html', root/'cv/index.html'):
    if page.exists():
        content = page.read_text()
        for placeholder in ('Write your biography here', 'You R. Name', 'Einstein', 'l762972374@stu.pku.edu.cn', '{{', '{%'):
            if placeholder in content: errors.append(f'{page}: placeholder {placeholder}')
if errors: raise SystemExit('\n'.join(errors))
print('All internal links, required pages, assets, and placeholder checks passed.')
