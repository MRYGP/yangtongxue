import re, glob

def validate_gate():
    text = ""
    for file in glob.glob('copies/*.md'):
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                text += f.read() + "\n"
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    ok = 1
    
    # Fairness 三句式至少两处
    fair = len(re.findall(r"Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; \(if involving accessibility\) challenge budget conservation\.", text))
    if fair < 2: 
        print(f"[FAIL] Fairness 三句式出现次数 < 2: {fair}")
        ok = 0
    else:
        print(f"[PASS] Fairness 三句式出现次数: {fair}")
    
    # 团队公式至少一处标准写法
    if not re.search(r"\$P_{2,\\mathrm\{team\}} \\ge B_{0,\\mathrm\{team\}} \+ \\delta\$", text):
        print("[FAIL] 团队公式标准写法未命中")
        ok = 0
    else:
        print("[PASS] 团队公式标准写法已命中")
    
    # 箭头统一至少命中一次
    if not re.search(r"S4→S1→S0", text):
        print("[FAIL] 未检测到标准箭头 S4→S1→S0")
        ok = 0
    else:
        print("[PASS] 检测到标准箭头 S4→S1→S0")
    
    # 输出 gate 结果
    print(f"\nGATE: {'PASS' if ok else 'FAIL'}")
    return ok

if __name__ == "__main__":
    validate_gate()