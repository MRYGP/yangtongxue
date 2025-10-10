import glob,os,re
chs=sorted(glob.glob("copies/CN_full_ch*.md"))
assert chs, "No CN_full_chXX.md found in copies/"

# 读取所有章节
content_parts = []
for p in chs:
    try:
        with open(p, encoding='utf-8', errors='ignore') as f:
            content_parts.append(f.read())
    except Exception as e:
        print(f"Error reading {p}: {e}")

# 合并内容
head="<!-- === CN_full_merged START === -->\n"
tail="\n<!-- === CN_full_merged END === -->\n"
txt=head + "\n\n".join(content_parts) + tail

# 添加必要的修复
txt = txt.replace("P ≥ B + δ", "$P_2 \\ge B_0 + \\delta$")
txt = txt.replace("P? ≥ B? + δ", "$P_2 \\ge B_0 + \\delta$")
txt = txt.replace("S4→S1至0", "S4→S1→S0")
txt = txt.replace("S4→S1逐步递减至0", "S4→S1→S0")

# 添加SSOT锚点
ssot_block = "> **SSOT**：所有术语与参数一律以 *CETG7.md §6 参数登记簿* 为准；正文出现的数值均标注 *working assumption / needs calibration*。"
if "SSOT" not in txt[:800]:
    txt = re.sub(r"(^# .*?\n)", r"\1\n" + ssot_block + "\n\n", txt, count=1, flags=re.M)

# 添加核心公式
if "$P_2 \\ge B_0 + \\delta$" not in txt:
    txt = re.sub(r"(^# .*?\n)", r"\1\n**核心公式**: $P_2 \\ge B_0 + \\delta$ (working assumption)\n\n", txt, count=1, flags=re.M)

# 添加Fairness三句式
fairness_text = "*Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; (if involving accessibility) challenge budget conservation.*"
txt = re.sub(r"(^# .*?\n)", r"\1\n" + fairness_text + "\n\n", txt, count=1, flags=re.M)

# 在方法部分添加第二个Fairness
txt = re.sub(r"(##\s*方法\b)", r"\1\n\n" + fairness_text + "\n", txt, count=1)

# 添加Goodhart脚注
goodhart_note = "*Note (Goodhart guard): This table supports direction and stratification only; do not push items as KPIs. Final judgment adheres to AVP (§3.0.2). Parameters are working assumptions and require calibration.*"
txt = re.sub(r"(\n\s*表\s*\d+.*?\n)(?!\*Note)", r"\1\n" + goodhart_note + "\n", txt, flags=re.S)

open("copies/CN_full_merged.md","w",encoding="utf-8").write(txt)
print("Regenerated CN_full_merged.md with all fixes.")