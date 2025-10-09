import re
p="copies/EN_full_merged.md"
t=open(p,encoding='utf-8',errors='ignore').read()
t=t.replace(""",'"').replace(""",'"').replace("'","'").replace("'","'")
t=re.sub(r"50\s*(?:-|–)\s*70%", "50–70%", t)
t=re.sub(r"\b4\s*(?:-|–)\s*8\s*weeks\b", "4–8 weeks", t)
open(p,"w",encoding="utf-8").write(t)
print("EN_full_merged.md normalized.")
