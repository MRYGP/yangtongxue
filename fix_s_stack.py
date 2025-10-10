import re,glob
for p in glob.glob("copies/*.md"):
    s=open(p,encoding="utf-8",errors="ignore").read()
    s=re.sub(r"S4→S1\s*(?:逐步递减)?至0", "S4→S1→S0", s)
    open(p,"w",encoding="utf-8").write(s)
print("Normalized S-stack to S4->S1->S0.")