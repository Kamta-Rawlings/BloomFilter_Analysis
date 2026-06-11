# experiment_hash_quality.py
# Compare how evenly different hash functions distribute values.

import csv
import os
import random
import string

from bloomfilter.hashing import HASHES

# Create results folder if it does not exist
os.makedirs("results", exist_ok=True)

# Reproducible random data
random.seed(2)

N = 20000  # number of test items
M = 200    # number of buckets

# Generate random strings
items = [
    "".join(random.choices(string.ascii_lowercase, k=8))
    for _ in range(N)
]

# Test each hash function
for name, fn in HASHES.items():

    counts = [0] * M

    # Count how many values fall into each bucket
    for item in items:
        bucket = fn(item) % M
        counts[bucket] += 1

    # Save histogram data
    output_file = f"results/hist_{name}.csv"

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["bucket", "count"])

        for bucket, count in enumerate(counts):
            writer.writerow([bucket, count])

    print(
        f"{name}: "
        f"min={min(counts)} "
        f"max={max(counts)} "
        f"mean={N/M:.1f}"
    )