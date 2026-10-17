#!/usr/bin/env python3
"""Generate the editor's on-demand Google Fonts index; never download font binaries.
Usage: python3 scripts/build-font-catalog.py /path/to/google-fonts-checkout
The checkout must include */*/METADATA.pb. See docs/font-catalog.md.
"""
import concurrent.futures, datetime, hashlib, json, pathlib, re, subprocess, sys, tempfile, urllib.parse
root = pathlib.Path(sys.argv[1])
revision = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
families = []
for path in sorted(root.glob('*/*/METADATA.pb')):
    source = path.read_text()
    name = re.search(r'^name: "(.*)"', source, re.M).group(1)
    category = re.search(r'^category: "(.*)"', source, re.M)
    license = re.search(r'^license: "(.*)"', source, re.M)
    axes = {re.search(r'tag: "(.*?)"', a).group(1): a for a in re.findall(r'^axes \{(.*?)^\}', source, re.M | re.S)}
    variants = []
    for font in re.findall(r'^fonts \{(.*?)^\}', source, re.M | re.S):
        style = re.search(r'style: "(.*?)"', font).group(1)
        weight = int(re.search(r'weight: (\d+)', font).group(1))
        weights = [weight]
        if 'wght' in axes:
            lo = float(re.search(r'min_value: ([\d.]+)', axes['wght']).group(1))
            hi = float(re.search(r'max_value: ([\d.]+)', axes['wght']).group(1))
            weights = sorted(set([weight] + [w for w in range(100,1001,100) if lo <= w <= hi]))
        variants.extend(str(w) + ('italic' if style == 'italic' else '') for w in weights)
    families.append(dict(family=name, category=(category.group(1).replace('_',' ').title() if category else 'Other'),
        license=license.group(1) if license else 'See license',
        licenseUrl=f'https://github.com/google/fonts/tree/{revision}/{path.parent.relative_to(root).as_posix()}',
        requested=sorted(set(variants)), variants=[]))
assert len(families) > 1500, 'Incomplete metadata checkout'
cache = pathlib.Path(tempfile.gettempdir()) / 'atypix-font-catalog-css'
cache.mkdir(exist_ok=True)
def fetch(group):
    query = '|'.join(f['family'] + ':' + ','.join(f['requested']) for f in group)
    url = 'https://fonts.googleapis.com/css?family=' + urllib.parse.quote(query, safe=':,|')
    path = cache / (hashlib.sha256(url.encode()).hexdigest()+'.css')
    if path.exists():
        css = path.read_text()
    else:
        result = subprocess.run(['curl','-sS','--max-time','60','--retry','2','--user-agent','AtypixCatalog/1.0','-w','\n%{http_code}',url],capture_output=True,text=True)
        if result.returncode: raise RuntimeError(result.stderr)
        css, status = result.stdout.rsplit('\n',1)
        if status == '400':
            if len(group) > 1:
                middle=len(group)//2; fetch(group[:middle]);fetch(group[middle:]);return
            group[0]['unavailable'] = 'Not currently served by Google Fonts';return
        if status != '200': raise RuntimeError(f'Google Fonts returned HTTP {status}; catalog not written')
        path.write_text(css)
    by_name={f['family']:f for f in group}
    for block in re.findall(r'@font-face\s*\{(.*?)\}',css,re.S):
        name=re.search(r"font-family:\s*['\"](.+?)['\"]",block).group(1)
        style=re.search(r'font-style:\s*(\w+)',block).group(1)
        weight=int(re.search(r'font-weight:\s*(\d+)',block).group(1))
        url=re.search(r'url\((https://fonts.gstatic.com/[^)]+\.ttf)\)',block)
        if name not in by_name: raise RuntimeError(f'Unexpected family {name}')
        if url:
            variant=dict(weight=weight,style=style,url=url.group(1))
            if variant not in by_name[name]['variants']:by_name[name]['variants'].append(variant)
    for f in group:
        if not f['variants']: f['unavailable']='No compatible static TTF provided by Google Fonts'
groups=[families[i:i+16] for i in range(0,len(families),16)]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for i,_ in enumerate(pool.map(fetch,groups),1):
        if i%10==0:print(f'{i}/{len(groups)} batches',flush=True)
for f in families:
    del f['requested']
    f['variants'].sort(key=lambda v:(v['style']!='normal',v['weight']))
output=dict(source='google/fonts',revision=revision,generated=datetime.date.today().isoformat(),families=families)
path=pathlib.Path(__file__).resolve().parent.parent/'assets/google-fonts.json'
path.write_text(json.dumps(output,ensure_ascii=False,separators=(',',':'))+'\n')
print(f'{len(families)} families; {sum(bool(f["variants"]) for f in families)} with static outlines; {path.stat().st_size} bytes')
