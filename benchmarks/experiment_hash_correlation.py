# experiment_hash_correlation.py
# Scatter (h1 mod M, h2 mod M) for pairs of hash functions.
# Independent hashes -> uniform cloud.
# Correlated hashes -> visible patterns / stripes.

import csv
import os
import random
import string

from bloomfilter.hashing import HASHES

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Make experiment reproducible
random.seed(3)

# Number of random strings to generate
N = 2000

# Modulus used for plotting coordinates
M = 500

# Generate random 8-character strings
items = [
    "".join(random.choices(string.ascii_lowercase, k=8))
    for _ in range(N)
]

# Hash function pairs to compare
pairs = [
    ("blake2_h1", "blake2_h2"),
    ("djb2", "sdbm"),
    ("djb2", "fnv1a")
]

for a, b in pairs:
    fa = HASHES[a]
    fb = HASHES[b]

    filename = f"results/corr_{a}_{b}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        # CSV header
        writer.writerow(["x", "y"])

        # Generate scatter coordinates
        for item in items:
            x = fa(item) % M
            y = fb(item) % M
            writer.writerow([x, y])

    print(f"Wrote {filename}")
