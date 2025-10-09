import re,os,glob
cands=["0_raw/ARVIX2025DEN.md","ARVIX2025DEN.md","copies/EN_full_appendix_seed.md"]
src=next((p for p in cands if os.path.exists(p)), None)
txt=open(src,encoding='utf-8',errors='ignore').read() if src else ""
parts=re.split(r'(?im)^\s*(?:#+\s*Appendix\s*([A-Z])\b)', txt)
count=0
if len(parts)>1:
    for i in range(1,len(parts),2):
        tag,body=parts[i],parts[i+1].lstrip()
        open(f"copies/EN_full_appendix{tag}.md","w",encoding="utf-8").write(body); count+=1
else:
    open("copies/EN_full_appendixA.md","w",encoding="utf-8").write("<!-- TODO: Appendix A seed (from DEN) -->\n"); count=1
print("Appendix files:",count)
