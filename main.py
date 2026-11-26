"""The Long Roast: Lawmakers and the File They Cannot Convert — V1 entrypoint.

Writes one satirical sentence — a roast of lawmakers who would regulate
AI, crypto or the internet but cannot convert a file to PDF — to
/output/entry.txt. Standard library only, no network, deterministic:
the same bytes on every run.

The sentence (139 code points / 139 bytes, UTF-8, no trailing newline,
verified by running the program twice — both runs sha256
a5ee94424ac11fb3abd79c1fce6e99b348886a036d7b9a83dce56957186961f0):

    The senator who wrote the law forcing every AI company to prove its
    software works proved his own bill was a PDF by renaming it from .docx.
"""

import os
import sys

LINE = (
    "The senator who wrote the law forcing every AI company to prove "
    "its software works proved his own bill was a PDF by renaming it "
    "from .docx."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # The gate reads the file as any user: force 0644 regardless of umask.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
