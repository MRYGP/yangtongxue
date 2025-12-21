from pathlib import Path

files = [
    "00_admin/SYNC.md",
    "00_admin/INDEX.md",
    "02_plans/2025-W52-plan.md",
    "03_logs/2025-W51-review.md",
]

for f in files:
    p = Path(f)
    content = p.read_text(encoding='utf-8')
    # Convert all line endings to LF
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    # Ensure file ends with exactly one newline
    content = content.rstrip('\n') + '\n'
    # Write as binary with LF only
    p.write_bytes(content.encode('utf-8'))
    print(f"{f}: normalized to LF (lines={content.count(chr(10))})")

