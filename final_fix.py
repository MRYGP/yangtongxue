import re

p = "copies/CN_full_merged.md"
t = open(p, encoding='utf-8', errors='ignore').read()

# 1. 添加第二个Fairness三句式到方法部分
fairness_text = "*Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; (if involving accessibility) challenge budget conservation.*"

# 查找方法部分标题
if "## 方法" in t:
    t = re.sub(r"(##\s*方法\b)", r"\1\n\n" + fairness_text + "\n", t, count=1)
else:
    # 如果没有找到方法标题，在第一个二级标题后添加
    t = re.sub(r"(^##\s*.*?\n)", r"\1\n" + fairness_text + "\n\n", t, count=1, flags=re.M)

# 2. 添加P2公式
if "$P_2 \\ge B_0 + \\delta$" not in t:
    # 在摘要或导言部分添加
    t = re.sub(r"(^# .*?\n)", r"\1\n**核心公式**: $P_2 \\ge B_0 + \\delta$ (working assumption)\n\n", t, count=1, flags=re.M)

# 3. 添加Goodhart脚注到表格
goodhart_note = "*Note (Goodhart guard): This table supports direction and stratification only; do not push items as KPIs. Final judgment adheres to AVP (§3.0.2). Parameters are working assumptions and require calibration.*"

# 查找表格并添加脚注
t = re.sub(r"(\n\s*表\s*\d+.*?\n)(?!\*Note)", r"\1\n" + goodhart_note + "\n", t, flags=re.S)

open(p, "w", encoding="utf-8").write(t)
print("Final fixes applied: added second Fairness, P2 formula, and Goodhart notes.")
