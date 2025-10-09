import re, glob, os

def search_patterns():
    patterns = [
        r'Cognitive Endosymbiosis|Cognitive Exoskeleton|Beneficial Cognitive Friction|Systematic Support Reduction|Layered Symbiosis Architecture|Partner-like Agency',
        r'50\s*[–-]\s*70%|4\s*[–-]\s*8\s*weeks|Cohen.?s d.?≥.?0\.3|≥\s*10%',
        r'S\s*4\s*(→|->|\\to)\s*S\s*1(\s*(→|->|\\to)\s*S\s*0)?',
        r'P_2|B_0|P\{2,\\mathrm\{team\}\}|B\{0,\\mathrm\{team\}\}',
        r'Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; \(if involving accessibility\) challenge budget conservation\.',
        r'Goodhart guard|not.*KPI|Final.*AVP'
    ]
    
    files = glob.glob('0_raw/*.md') + glob.glob('copies/*.md')
    results = []
    
    for pattern in patterns:
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
                    for match in matches:
                        line_num = content[:match.start()].count('\n') + 1
                        line_content = content.split('\n')[line_num - 1]
                        results.append(f"{file}:{line_num}:{line_content.strip()}")
            except Exception as e:
                print(f"Error reading {file}: {e}")
    
    with open('reports/consistency_hits.txt', 'w', encoding='utf-8') as f:
        for result in results:
            f.write(result + '\n')
    
    print(f"Found {len(results)} matches, saved to reports/consistency_hits.txt")

if __name__ == "__main__":
    search_patterns()
