import re
p="copies/CN_full_merged.md"
t=open(p,encoding='utf-8',errors='ignore').read()
t=re.sub(r"(LSA[-–]F（功能分层）.*?\n)", r"\1**声明：L1–L4 仅为功能层；S4–S1–S0 仅表支持强度；二者正交、互不表示。**\n", t, count=1, flags=re.S)
open(p,"w",encoding="utf-8").write(t)
print("Emphasized orthogonality L1–L4 vs S4–S1–S0.")
