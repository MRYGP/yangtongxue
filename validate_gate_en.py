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
    
    # Check Fairness 三句式 at least twice
    fair = len(re.findall(r"Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; \(if involving accessibility\) challenge budget conservation\.", text))
    if fair < 2: 
        print(f"[FAIL] Fairness 三句式 count < 2: {fair}")
        ok = 0
    else:
        print(f"[PASS] Fairness 三句式 count: {fair}")
    
    # Check team formula standard format
    if not re.search(r"\$P_{2,\\mathrm\{team\}} \\ge B_{0,\\mathrm\{team\}} \+ \\delta\$", text):
        print("[FAIL] Team formula standard format not found")
        ok = 0
    else:
        print("[PASS] Team formula standard format found")
    
    # Check arrow unification
    if not re.search(r"S4→S1→S0", text):
        print("[FAIL] Standard arrow S4→S1→S0 not found")
        ok = 0
    else:
        print("[PASS] Standard arrow S4→S1→S0 found")
    
    # Output gate result
    print(f"\nGATE: {'PASS' if ok else 'FAIL'}")
    return ok

if __name__ == "__main__":
    validate_gate()