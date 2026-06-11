# experiment_compression.py
# Compare memory usage of a Python set and a Bloom filter.
# Varies both expected number of items (n) and target false positive rate (p).

import csv
import os
import sys
from bloomfilter import BloomFilter

# Expected number of items
SIZES = [1000, 10000, 100000]

# Target false positive rates
FPRS = [0.1, 0.01, 0.001]

os.makedirs("results", exist_ok=True)

rows = []

for n in SIZES:
    # Build reference Python set
    s = set()
    for i in range(n):
        s.add("item-" + str(i))

    set_bytes = sys.getsizeof(s) + sum(sys.getsizeof(x) for x in s)

    for p in FPRS:

        # Build Bloom filter
        bf = BloomFilter(n, p)

        for i in range(n):
            bf.add("item-" + str(i))

        bloom_bytes = bf.m // 8

        compression = set_bytes / bloom_bytes

        rows.append({
            "n": n,
            "target_fpr": p,
            "set_bytes": set_bytes,
            "bloom_bytes": bloom_bytes,
            "compression_ratio": compression,
        })

        print(
            "n=%d  p=%g  set=%d B  bloom=%d B  ratio=%.1fx"
            % (
                n,
                p,
                set_bytes,
                bloom_bytes,
                compression,
            )
        )

with open("results/experiment_compression.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "n",
            "target_fpr",
            "set_bytes",
            "bloom_bytes",
            "compression_ratio",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)

print("wrote results/experiment_compression.csv")
