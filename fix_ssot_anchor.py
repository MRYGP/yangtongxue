import re
p="copies/CN_full_merged.md"
t=open(p,encoding='utf-8',errors='ignore').read()
blk="> **SSOT**：所有术语与参数一律以 *CETG7.md §6 参数登记簿* 为准；正文出现的数值均标注 *working assumption / needs calibration*。"
if "SSOT" not in t[:800]:
    t=re.sub(r"(^# .*?\n)", r"\1\n"+blk+"\n\n", t, count=1, flags=re.M)
open(p,"w",encoding="utf-8").write(t); print("Inserted SSOT hard anchor at top.")
