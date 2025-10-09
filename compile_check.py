import re,sys,io
t=open("copies/EN_full_merged.md",encoding='utf-8',errors='ignore').read()
fences=t.count("```")
print("[PASS] Code fences balanced." if fences%2==0 else f"[FAIL] Code fences not balanced: {fences}")
unclosed = re.findall(r"\$[^$\n]*$", t, flags=re.M)
print(f"[WARN] trailing inline LaTeX lines: {len(unclosed)}")
