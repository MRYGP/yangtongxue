import re

def fix_bullets():
    with open('copies/EN_full_merged.md', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 删除特定列表项前面的破折号
    patterns_to_fix = [
        r'^- 1\.1 Core Proposition: A New Standard for Evaluating AI',
        r'^- 1\.2 Theoretical Gaps: Shared Blind Spots in Existing Paradigms', 
        r'^- 1\.3 CET\'s Core Contributions',
        r'^- 1\.4 Methodology and Paper Structure'
    ]
    
    for pattern in patterns_to_fix:
        content = re.sub(pattern, lambda m: m.group(0)[2:], content, flags=re.MULTILINE)
    
    # 也处理可能的其他格式
    content = re.sub(r'^- 1\.1 Core Proposition: A New Standard for Evaluating AI', '1.1 Core Proposition: A New Standard for Evaluating AI', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.2 Theoretical Gaps: Shared Blind Spots in Existing Paradigms', '1.2 Theoretical Gaps: Shared Blind Spots in Existing Paradigms', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.3 CET\'s Core Contributions', '1.3 CET\'s Core Contributions', content, flags=re.MULTILINE)
    content = re.sub(r'^- 1\.4 Methodology and Paper Structure', '1.4 Methodology and Paper Structure', content, flags=re.MULTILINE)
    
    with open('copies/EN_full_merged_fixed_bullets.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed bullet points and saved as EN_full_merged_fixed_bullets.md")

if __name__ == "__main__":
    fix_bullets()
