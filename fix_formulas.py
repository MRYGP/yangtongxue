import re,glob,io
paths=[p for p in glob.glob("copies/*.md") if "merged" in p or "ch0" in p]
for p in paths:
    s=open(p,encoding="utf-8",errors="ignore").read()
    s=re.sub(r"P\s*≥\s*B\s*\+\s*δ", r"$P_2 \\ge B_0 + \\delta$", s)
    s=re.sub(r"P\?\s*≥\s*B\?\s*\+\s*δ", r"$P_2 \\ge B_0 + \\delta$", s)
    # 兜底把裸的 P2/B0 也标准化为 LaTeX
    s=re.sub(r"\bP2\s*≥\s*B0\s*\+\s*δ\b", r"$P_2 \\ge B_0 + \\delta$", s)
    open(p,"w",encoding="utf-8").write(s)
print("Fixed corrupted P/B formulas.")
