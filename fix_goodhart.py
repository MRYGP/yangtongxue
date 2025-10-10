import re,glob
note="*Note (Goodhart guard): This table supports direction and stratification only; do not push items as KPIs. Final judgment adheres to AVP (§3.0.2). Parameters are working assumptions and require calibration.*"
for p in glob.glob("copies/*.md"):
    t=open(p,encoding='utf-8',errors='ignore').read()
    t=re.sub(r"(\n\s*表\s*\d+.*?\n)(?!\*Note)", r"\1\n"+note+"\n", t, flags=re.S)
    t=re.sub(r"(\n\s*Table\s*\d+.*?\n)(?!\*Note)", r"\1\n"+note+"\n", t, flags=re.S)
    open(p,"w",encoding="utf-8").write(t)
print("Appended Goodhart notes under tables.")
