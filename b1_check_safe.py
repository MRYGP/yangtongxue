import re,glob
pats=[
 r"S4\s*→\s*S1(?:\s*→\s*S0)?",
 r"50–70%",
 r"4–8\s*weeks",
 r"Cohen.?s d\s*≥\s*0\.3",
 r"\$P_{2,\\mathrm\{team\}} \\ge B_{0,\\mathrm\{team\}} \+ \\delta\$",
 r"BCI×0\.4\s*\+\s*ICR×0\.6",
]
report=[]
targets=sorted(glob.glob("copies/EN_full_ch0[4-6].md")+glob.glob("copies/EN_full_appendix*.md")+["copies/EN_full_refs.md"])
for f in targets:
    try: t=open(f,encoding='utf-8',errors='ignore').read()
    except: 
        report.append(f"[MISS] {f} (cannot open)"); continue
    miss=[p for p in pats if not re.search(p,t)]
    if miss: report.append(f"[WARN] {f} missing: " + ", ".join(miss))
open("reports/consistency_hits_after_replace.txt","a",encoding="utf-8").write("\n".join(report)+"\n")
if report:
    for line in report:
        print(line)
else:
    print("A2 check: OK")
