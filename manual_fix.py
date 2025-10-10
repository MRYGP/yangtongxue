import re

# 读取文件
with open("copies/CN_full_merged.md", encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. 添加第二个Fairness三句式
fairness_text = "*Adjust task format without lowering challenge intensity; assess by relative improvement rather than absolute level; (if involving accessibility) challenge budget conservation.*"

# 查找方法部分并添加
if "## 方法" in content:
    content = content.replace("## 方法", "## 方法\n\n" + fairness_text + "\n")
else:
    # 在第一个二级标题后添加
    content = re.sub(r"(^##\s*.*?\n)", r"\1\n" + fairness_text + "\n\n", content, count=1, flags=re.M)

# 2. 添加Goodhart脚注到表格
goodhart_note = "*Note (Goodhart guard): This table supports direction and stratification only; do not push items as KPIs. Final judgment adheres to AVP (§3.0.2). Parameters are working assumptions and require calibration.*"

# 查找表格并添加脚注
content = re.sub(r"(\n\s*表\s*\d+.*?\n)(?!\*Note)", r"\1\n" + goodhart_note + "\n", content, flags=re.S)

# 写回文件
with open("copies/CN_full_merged.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Manual fixes applied.")
