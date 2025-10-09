import re

def clean_markdown():
    with open('copies/EN_full_merged.md', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 清理常见的编码问题
    content = content.replace('"', '"').replace('"', '"')
    content = content.replace(''', "'").replace(''', "'")
    content = content.replace('–', '-').replace('—', '--')
    content = content.replace('…', '...')
    
    # 修复LaTeX数学符号
    content = re.sub(r'\\geq(?![a-zA-Z])', r'$\\geq$', content)
    content = re.sub(r'\\leq(?![a-zA-Z])', r'$\\leq$', content)
    content = re.sub(r'\\to(?![a-zA-Z])', r'$\\to$', content)
    content = re.sub(r'\\delta(?![a-zA-Z])', r'$\\delta$', content)
    content = re.sub(r'\\alpha(?![a-zA-Z])', r'$\\alpha$', content)
    content = re.sub(r'\\beta(?![a-zA-Z])', r'$\\beta$', content)
    content = re.sub(r'\\gamma(?![a-zA-Z])', r'$\\gamma$', content)
    
    # 清理其他特殊字符
    content = re.sub(r'[^\x00-\x7F]+', '?', content)
    
    with open('copies/EN_full_merged_clean.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Cleaned markdown saved as EN_full_merged_clean.md")

if __name__ == "__main__":
    clean_markdown()
