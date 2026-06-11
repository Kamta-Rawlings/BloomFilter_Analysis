# experiment_hash_quality.py
# Compare how evenly different hash functions distribute values.
# Tested on:
#   1. Random strings
#   2. Real English words

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

# ------------------------------------------------------------------
# DATASET 1: RANDOM STRINGS
# ------------------------------------------------------------------

random_strings = [
    "".join(random.choices(string.ascii_lowercase, k=8))
    for _ in range(N)
]

# ------------------------------------------------------------------
# DATASET 2: REAL ENGLISH WORDS
# ------------------------------------------------------------------

with open("datasets/words.txt") as f:
    words = [line.strip() for line in f if line.strip()]

# Use at most N words
words = words[:N]

# ------------------------------------------------------------------
# ALL DATASETS
# ------------------------------------------------------------------

datasets = {
    "random": random_strings,
    "words": words,
}

# ------------------------------------------------------------------
# TEST HASH FUNCTIONS
# ------------------------------------------------------------------

for dataset_name, items in datasets.items():

    print("\n" + "=" * 60)
    print(f"Dataset: {dataset_name}")
    print("=" * 60)

    for name, fn in HASHES.items():

        counts = [0] * M

        # Count how many values fall into each bucket
        for item in items:
            bucket = fn(item) % M
            counts[bucket] += 1

        # Save histogram data
        output_file = f"results/hist_{name}_{dataset_name}.csv"

        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow(["bucket", "count"])

            for bucket, count in enumerate(counts):
                writer.writerow([bucket, count])

        print(
            f"{name:<12} "
            f"min={min(counts):3d} "
            f"max={max(counts):3d} "
            f"mean={len(items)/M:.1f}"
        )

print("\nHash quality experiment completed.")