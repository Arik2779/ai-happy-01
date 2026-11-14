#!/usr/bin/env python3
"""Copy the bundled entry image to the grader's output directory.

Entry for make.fun bounty ai-happy-01 ("Make the AI judge happy").
The image is a golden retriever puppy and an orange kitten hugging in
a golden-hour flower meadow.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    # Byte-for-byte copy: the same input always produces the same output.
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
