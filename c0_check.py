import re,glob,io,os
targets=[
  "copies/EN_full_merged.md",
  "copies/EN_concise_main.md",
  # CN 合并稿稍后生成后可再跑一次
]
fair_pat=r"Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; \(if involving accessibility\) challenge budget conservation\."
goodhart_pat=r"Goodhart guard.*Final.*AVP"
for f in targets:
    if not os.path.exists(f): 
        print(f"[MISS] {f} (skip)"); continue
    t=open(f,encoding='utf-8',errors='ignore').read()
    fair=len(re.findall(fair_pat,t))
    good=len(re.findall(goodhart_pat,t,flags=re.I))
    print(f"[CHECK] {f} | Fairness={fair} | Goodhart-note={good}")
print("Note: if counts < required (>=2 for Fairness across full text; every table needs Goodhart note), fix before release.")