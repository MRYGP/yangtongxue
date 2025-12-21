from pathlib import Path

TARGETS = [
    "00_admin/SYNC.md",
    "00_admin/INDEX.md",
    "02_plans/2025-W52-plan.md",
    "03_logs/2025-W51-review.md",
]

for rel in TARGETS:
    p = Path(rel)
    b = p.read_bytes()
    s = b.decode("utf-8", errors="replace")
    # convert CRLF + CR -> LF
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    # ensure file ends with exactly one newline
    s = s.rstrip("\n") + "\n"
    p.write_text(s, encoding="utf-8")
    print(f"{rel}: lines={s.count(chr(10))}")

