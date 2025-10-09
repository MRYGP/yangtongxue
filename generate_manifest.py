import re, os, csv, glob, sys
files = sorted(glob.glob('0_raw/*.md'))
rows=[['version(lang)','chapter','path','status','needs_fix']]

def classify(fn):
    basename = os.path.basename(fn)
    if re.match(r'CETG\d+\.md$', basename): return ('CN-Full', re.findall(r'\d+',basename)[0])
    if basename in ['Chapter 4.md','Chapter 5+6.md','Chapter 5.md','Chapter 6.md','References.md']: return ('EN-Full','ch?')  # 细化见下
    if re.match(r'ARVIX2025[ABCD]EN\.md$', basename): return ('EN-Full','part-'+basename[9]) # A/B/C/D
    if re.match(r'ARVIX2025[ABCD]\.md$', basename): return ('EN-Concise','part-'+basename[9])
    # 可能存在的中文简版主文件（若后续补上会自动归类）
    if re.search(r'CN.*concise', basename, re.I): return ('CN-Concise','main')
    return ('Unclassified','-')

def needs_fix_flags(text):
    flags=[]
    if '"' in text or '"' in text or "'" in text or "'" in text: flags.append('quotes')
    if re.search(r'\\text\{|\\mathrm\{|\\to|\\geq|\\leq|\$.*\$', text): flags.append('latex')
    if re.search(r'S\s*4\s*(→|->|\\to)\s*S\s*1(\s*(→|->|\\to)\s*S\s*0)?', text) and not re.search(r'S4→S1→S0', text): flags.append('arrows')
    if re.search(r'50\s*[–-]\s*70\%|4\s*[–-]\s*8 weeks|Cohen.?s d.?≥.?0\.3|≥\s*10\%', text, re.I): pass
    else: flags.append('params/anchors')
    return '|'.join(sorted(set(flags))) or 'none'

for fn in files:
    ver, chap = classify(fn)
    status = 'partial' if os.path.basename(fn) in ['Chapter 5+6.md'] else 'complete'
    if ver=='Unclassified': status='review'
    try:
        with open(fn,'r',encoding='utf-8',errors='ignore') as f:
            txt=f.read()
        nf = needs_fix_flags(txt)
    except Exception:
        nf = 'scan_error'
    rows.append([ver+'('+('CN' if ver.startswith('CN') else 'EN' if ver!='Unclassified' else '?')+')', chap, fn, status, nf])

os.makedirs('inventory', exist_ok=True)
with open('inventory/manifest.csv','w',newline='',encoding='utf-8') as f:
    csv.writer(f).writerows(rows)

print('Wrote inventory/manifest.csv with', len(rows)-1, 'entries.')