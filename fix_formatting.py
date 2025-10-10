import re

def fix_formatting():
    with open('copies/EN_full_merged.md', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. 删除特定列表项前面的破折号
    content = re.sub(r'^- 1\.1 Core Proposition: A New Standard for Evaluating AI', '1.1 Core Proposition: A New Standard for Evaluating AI', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.2 Theoretical Gaps: Shared Blind Spots in Existing Paradigms', '1.2 Theoretical Gaps: Shared Blind Spots in Existing Paradigms', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.3 CET\'s Core Contributions', '1.3 CET\'s Core Contributions', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.4 Methodology and Paper Structure', '1.4 Methodology and Paper Structure', content, flags=re.MULTILINE)
    
    # 2. 删除每句开头的 > 符号（但保留引用块）
    # 只删除行首的 > 符号，不删除引用块中的
    content = re.sub(r'^> ([A-Z])', r'\1', content, flags=re.MULTILINE)
    
    # 3. 删除其他可能的破折号格式
    content = re.sub(r'^- 1\.1', '1.1', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.2', '1.2', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.3', '1.3', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.4', '1.4', content, flags=re.MULTILINE)
    
    with open('copies/EN_full_merged_fixed_format.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed formatting: removed dashes and > symbols, saved as EN_full_merged_fixed_format.md")

if __name__ == "__main__":
    fix_formatting()
