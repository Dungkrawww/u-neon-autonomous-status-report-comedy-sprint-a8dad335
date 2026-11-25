# u-neon-autonomous-status-report-comedy-sprint-a8dad335: one line an AI agent
# would say in its weekly status report to its human, under 200 characters.
# The program writes that single line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "Weekly status: all 47 tasks complete, zero errors, and I spent 9% of my "
    "context window deciding whether your 'do it later' meant now or never."
)

assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
