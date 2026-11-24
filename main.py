"""Write the one-line Monday review to entry.txt.

The review is Monday as a squatter who never leaves: it slips in on
Sunday night, rearranges my sleep, and then — the punch — starts
charging me rent for the week it stole.
"""

import os

LINE = "Monday moved in on Sunday night, rearranged my sleep, and is now charging me rent."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
