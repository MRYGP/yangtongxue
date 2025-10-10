import re
blk="*Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; (if involving accessibility) challenge budget conservation.*"
for p in ["copies/CN_full_merged.md","copies/EN_full_merged.md"]:
    t=open(p,encoding='utf-8',errors='ignore').read()
    # 在第一个一级标题后注入一次；在"方法/Method"标题后再注入一次
    t=re.sub(r"(^# .*?\n)", r"\1\n"+blk+"\n\n", t, count=1, flags=re.M)
    t=re.sub(r"(^##\s*(方法|Methods?)\b.*?\n)", r"\1\n"+blk+"\n\n", t, count=1, flags=re.M|re.I)
    open(p,"w",encoding="utf-8").write(t)
print("Injected Fairness tri-sentence twice.")
