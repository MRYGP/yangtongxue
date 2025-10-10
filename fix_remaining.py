import re

# 1. 在方法部分添加第二个Fairness三句式
p = "copies/CN_full_merged.md"
t = open(p, encoding='utf-8', errors='ignore').read()

# 查找方法部分并添加Fairness三句式
fairness_text = "*Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; (if involving accessibility) challenge budget conservation.*"

# 在方法部分添加
t = re.sub(r"(##\s*方法\b.*?\n)", r"\1\n" + fairness_text + "\n\n", t, count=1, flags=re.M|re.I)

# 2. 确保有正确的P2公式
t = re.sub(r"P\?\s*=\s*B0\s*\+\s*d", r"$P_2 \\ge B_0 + \\delta$", t)

# 3. 确保Goodhart脚注格式正确
goodhart_note = "*Note (Goodhart guard): This table supports direction and stratification only; do not push items as KPIs. Final judgment adheres to AVP (§3.0.2). Parameters are working assumptions and require calibration.*"

# 在表格后添加标准脚注
t = re.sub(r"(\n\s*表\s*\d+.*?\n)(?!\*Note)", r"\1\n" + goodhart_note + "\n", t, flags=re.S)

open(p, "w", encoding="utf-8").write(t)
print("Fixed remaining issues: added second Fairness, fixed P2 formula, standardized Goodhart notes.")