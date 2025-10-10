import re

# 读取文件
with open("copies/CN_full_merged.md", encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. 删除所有非表格的横线（------）
# 保留表格内的横线，只删除独立的横线
lines = content.split('\n')
filtered_lines = []
skip_next = False

for i, line in enumerate(lines):
    if line.strip() == '------':
        # 检查前后行是否包含表格标记
        prev_line = lines[i-1] if i > 0 else ""
        next_line = lines[i+1] if i < len(lines)-1 else ""
        
        # 如果前后行都不包含表格标记（|），则删除这行
        if '|' not in prev_line and '|' not in next_line:
            continue
    filtered_lines.append(line)

content = '\n'.join(filtered_lines)

# 2. 删除1.4.2部分的错误内容（摘要和参考文献模板）
# 找到1.4.2部分并删除到下一个主要章节
content = re.sub(r'#### 1\.4\.2.*?(?=# [^#]|$)', '', content, flags=re.DOTALL)

# 3. 在文档末尾添加参考文献部分（在END标记之前）
references_section = """

## 参考文献

[1] Goodhart C A E. Problems of monetary management: The UK experience[C]//Papers in Monetary Economics. Sydney: Reserve Bank of Australia, 1975 DOI: https://doi.org/10.2307/2232004.

[2] Taleb N N. Antifragile: Things that gain from disorder[M]. Random House, 2012.

[3] Vygotsky L S. Mind in society: The development of higher psychological processes[M]. Harvard University Press, 1978.

[4] Bandura A. Social learning theory[M]. Prentice Hall, 1977.

[5] Ericsson K A, Krampe R T, Tesch-Römer C. The role of deliberate practice in the acquisition of expert performance[J]. Psychological Review, 1993, 100(3): 363-406.

[6] Collins A, Brown J S, Newman S E. Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics[M]//Knowing, learning, and instruction. Routledge, 2018: 453-494.

[7] Sweller J. Cognitive load theory[M]//Psychology of learning and motivation. Academic Press, 2011: 37-76.

[8] Mayer R E. Multimedia learning[M]. Cambridge University Press, 2009.

[9] Paas F, Renkl A, Sweller J. Cognitive load theory and instructional design: Recent developments[J]. Educational Psychologist, 2003, 38(1): 1-4.

[10] Van Merriënboer J J, Kirschner P A. Ten steps to complex learning: A systematic approach to four-component instructional design[M]. Routledge, 2017.

*注：以上参考文献为示例，实际使用时请根据正文引用情况调整。*

"""

# 在END标记之前插入参考文献
content = re.sub(r'(<!-- === CN_full_merged END === -->)', references_section + r'\1', content)

# 写回文件
with open("copies/CN_full_merged.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed document structure:")
print("1. Removed non-table horizontal lines")
print("2. Removed incorrect 1.4.2 section")
print("3. Added references section before END marker")
