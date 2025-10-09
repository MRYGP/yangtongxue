import re,os,io
srcs=["0_raw/Chapter 5+6.md","0_raw/Chapter 5.md"]
src=None
for s in srcs:
    if os.path.exists(s): src=s; break
assert src, "No Chapter 5+6.md or Chapter 5.md found in 0_raw/"
t=open(src,encoding='utf-8',errors='ignore').read()

# 以 "Chapter 6 / # 6 / 6" 等标题切分
m=re.split(r'(?im)^\s*(?:#+\s*Chapter\s*6\b|#+\s*6\b|Chapter\s*6\b)\s*',t,maxsplit=1)
if len(m)==2:
    ch5=re.sub(r'(?im)^\s*(?:#+\s*Chapter\s*5\b|#+\s*5\b|Chapter\s*5\b)\s*','',m[0],count=1).lstrip()
    ch6=m[1].lstrip()
else:
    ch5=t
    ch6="<!-- TODO: split from Chapter 5+6.md -->\n"+t

os.makedirs("copies",exist_ok=True)
open("copies/EN_full_ch05.md","w",encoding="utf-8").write(ch5)
open("copies/EN_full_ch06.md","w",encoding="utf-8").write(ch6)
print("Wrote copies/EN_full_ch05.md and copies/EN_full_ch06.md")
