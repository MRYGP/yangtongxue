import re,glob
pat=r"δ\s*≥\s*0\.3\s*SD\s*或\s*10%.*?(?:SD\s*或\s*10%)?"
rep="Cohen's d ≥ 0.3 或 ≥10%（*working assumption*）"
for p in glob.glob("copies/*.md"):
    s=open(p,encoding="utf-8",errors="ignore").read()
    s=re.sub(pat, rep, s)
    s=re.sub(r"Cohen.?s d\s*(?:≥|>=)\s*0\.3(?!\s*或\s*≥?10%)", "Cohen's d ≥ 0.3 或 ≥10%（*working assumption*）", s)
    open(p,"w",encoding="utf-8").write(s)
print("Unified delta threshold phrasing.")
