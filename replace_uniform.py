import re, glob, os

def replace_uniform():
    files = glob.glob('copies/*.md')
    
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 统一箭头：S4→S1→S0
            content = re.sub(r'S\s*_?4\s*(?:\\to|->|→)\s*S\s*_?1\s*(?:\\to|->|→)\s*S\s*_?0', 'S4→S1→S0', content)
            content = re.sub(r'S\s*_?4\s*(?:\\to|->|→)\s*S\s*_?1', 'S4→S1', content)
            
            # 统一范围与连字符
            content = re.sub(r'50\s*(?:-|–|\\text\{–\})\s*70%', '50–70%', content)
            content = re.sub(r'\b4\s*(?:-|–|\\text\{–\})\s*8\s*weeks\b', '4–8 weeks', content)
            
            # δ 与效应量写法
            content = re.sub(r"Cohen.?s d\s*(?:>=|≥)\s*0\.3(?:\s*\(.*?\))?", "Cohen's d ≥ 0.3 (working assumption)", content, flags=re.IGNORECASE)
            content = re.sub(r'\$\s*\\delta\s*\\geq\s*0\.3\s*,\s*\\mathrm\{SD\}\s*\$', r'$\delta \ge 0.3\,\mathrm{SD}$ (working assumption)', content)
            
            # 团队公式统一
            content = re.sub(r'\$P\{?2,\\mathrm\{team\}\}?[^$]*?\$|\$B\{?0,\\mathrm\{team\}\}?[^$]*?\$', r'$P_{2,\mathrm{team}} \ge B_{0,\mathrm{team}} + \delta$', content)
            
            # 引号统一
            content = content.replace('"', '"').replace('"', '"')
            content = content.replace(''', "'").replace(''', "'")
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Processed {file}")
            
        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    replace_uniform()
    print("Replacement completed")
