import re

def fix_latex():
    with open('copies/EN_full_merged_clean.md', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 修复LaTeX数学模式问题
    content = re.sub(r'\\mathrm\{([^}]+)\}', r'$\\mathrm{\1}$', content)
    content = re.sub(r'\\text\{([^}]+)\}', r'$\\text{\1}$', content)
    
    # 修复P_{2,\mathrm{team}}这样的表达式
    content = re.sub(r'P_\{2,\\mathrm\{team\}\}', r'$P_{2,\\mathrm{team}}$', content)
    content = re.sub(r'B_\{0,\\mathrm\{team\}\}', r'$B_{0,\\mathrm{team}}$', content)
    
    # 修复其他数学符号
    content = re.sub(r'(?<!\$)\\geq(?!\$)', r'$\\geq$', content)
    content = re.sub(r'(?<!\$)\\leq(?!\$)', r'$\\leq$', content)
    content = re.sub(r'(?<!\$)\\to(?!\$)', r'$\\to$', content)
    content = re.sub(r'(?<!\$)\\delta(?!\$)', r'$\\delta$', content)
    content = re.sub(r'(?<!\$)\\times(?!\$)', r'$\\times$', content)
    
    with open('copies/EN_full_merged_fixed.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed LaTeX syntax saved as EN_full_merged_fixed.md")

if __name__ == "__main__":
    fix_latex()