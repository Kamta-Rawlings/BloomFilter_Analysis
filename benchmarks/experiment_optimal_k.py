# experiment_optimal_k.py
# Measure how the false positive rate changes as the
# number of hash functions (k) varies.

import csv
import math
import os
import random
import string

from bitarray import bitarray

from bloomfilter import BloomFilter

os.makedirs("results", exist_ok=True)

# Experiment settings
n = 5000          # inserted items
m = 50000         # fixed filter size
ks = range(1, 16)

random.seed(0)


def random_string():
    return "".join(random.choices(string.ascii_letters, k=8))


# Generate datasets
inserted = [random_string() for _ in range(n)]

tested = [random_string() for _ in range(20000)]
tested = [x for x in tested if x not in set(inserted)]

rows = []

for k in ks:

    bf = BloomFilter(n, 0.01)

    # Override automatically computed values
    bf.m = m
    bf.k = k
    bf.bits = bitarray(m)
    bf.bits.setall(False)
    bf.count = 0

    # Insert items
    for word in inserted:
        bf.add(word)

    # Measure false positives
    false_positives = sum(1 for word in tested if word in bf)

    measured_fpr = false_positives / len(tested)

    # Theoretical Bloom filter FPR
    theoretical_fpr = (1 - math.exp(-k * n / m)) ** k

    rows.append({
        "k": k,
        "measured_fpr": measured_fpr,
        "theoretical_fpr": theoretical_fpr,
    })

    print(
        f"k={k:2d}  "
        f"measured={measured_fpr:.4f}  "
        f"theory={theoretical_fpr:.4f}"
    )

# Save results
with open("results/experiment_optimal_k.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["k", "measured_fpr", "theoretical_fpr"]
    )
    writer.writeheader()
    writer.writerows(rows)

print("done")
