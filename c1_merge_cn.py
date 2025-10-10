import glob,os
chs=sorted(glob.glob("copies/CN_full_ch*.md"))
assert chs, "No CN_full_chXX.md found in copies/"
head="<!-- === CN_full_merged START === -->\n"
tail="\n<!-- === CN_full_merged END === -->\n"
txt=head + "\n\n".join(open(p,encoding="utf-8",errors="ignore").read() for p in chs) + tail
open("copies/CN_full_merged.md","w",encoding="utf-8").write(txt)
print("Wrote copies/CN_full_merged.md")
