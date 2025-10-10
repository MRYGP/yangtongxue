import re,io
p="copies/CN_full_merged.md"
t=open(p,encoding='utf-8',errors='ignore').read()
ok=1

# 检查Fairness三句式（简化匹配）
fairness_count = len(re.findall(r"Adjust task format without lowering challenge intensity", t))
print(f"Fairness count: {fairness_count}")

# 检查S4→S1→S0
has_s_stack = "S4→S1→S0" in t
print(f"Has S4->S1->S0: {has_s_stack}")

# 检查P2公式（简化匹配）
has_p2_formula = "$P_2 \\ge B_0 + \\delta$" in t
print(f"Has P2 formula: {has_p2_formula}")

# 检查Goodhart脚注
has_goodhart = "Goodhart guard" in t
print(f"Has Goodhart: {has_goodhart}")

tests={
 "Fairness tri-sentence (>=2)": fairness_count >= 2,
 "Has S4->S1->S0": has_s_stack,
 "Has P2 >= B0 + delta": has_p2_formula,
 "Has Goodhart notes": has_goodhart
}
for k,v in tests.items():
    print(("PASS" if v else "FAIL"), "-", k); ok &= v
print("GATE:", "PASS" if ok else "FAIL")
