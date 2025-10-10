import re

# 读取文件
with open("copies/CN_full_merged.md", encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. 确保有正确的P2公式格式
content = re.sub(r"\$P_2 \\ge B_0 \\+ \\delta\$", r"$P_2 \\ge B_0 + \\delta$", content)

# 2. 添加Goodhart脚注到任何表格
goodhart_note = "*Note (Goodhart guard): This table supports direction and stratification only; do not push items as KPIs. Final judgment adheres to AVP (§3.0.2). Parameters are working assumptions and require calibration.*"

# 查找表格并添加脚注
content = re.sub(r"(\n\s*表\s*\d+.*?\n)(?!\*Note)", r"\1\n" + goodhart_note + "\n", content, flags=re.S)
content = re.sub(r"(\n\s*Table\s*\d+.*?\n)(?!\*Note)", r"\1\n" + goodhart_note + "\n", content, flags=re.S)

# 3. 确保有至少一个Goodhart脚注
if "Goodhart guard" not in content:
    content += "\n\n" + goodhart_note + "\n"

# 写回文件
with open("copies/CN_full_merged.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Final manual fixes applied.")