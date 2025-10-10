import re,io
def inject(path,lines):
    t=open(path,encoding='utf-8',errors='ignore').read()
    if "DOI:" in t[:500]: 
        print(f"[SKIP] {path} already has DOI block"); return
    block="\n".join([
        "<!-- Publication Links -->",
        "**DOI (Zenodo CN Full)**: [pending]",
        "**OSF (EN Full)**: [pending]",
        "**SSRN**: [pending]",
        ""
    ])
    # 在文首首个标题后注入
    t=re.sub(r"(^# .*\n)", r"\1"+block, t, count=1, flags=re.M)
    if t==open(path,encoding='utf-8',errors='ignore').read(): 
        t=block+"\n"+t
    open(path,"w",encoding="utf-8").write(t)
    print(f"[OK] injected DOI block into {path}")

for p in ["copies/CN_full_merged.md","copies/EN_full_merged.md","copies/EN_concise_main.md"]:
    try: inject(p,[])
    except Exception as e: print("[ERR]",p,e)
