# experiment_size.py
# Vary filter size m for fixed n. FPR should decrease as m increases.

import csv
import os
import random
import string
import math

from bitarray import bitarray
from bloomfilter import BloomFilter

os.makedirs("results", exist_ok=True)

random.seed(1)


def random_string():
    return "".join(random.choices(string.ascii_letters, k=8))


n = 3000
ms = [5000, 10000, 20000, 40000, 80000, 160000]

inserted = [random_string() for _ in range(n)]
inserted_set = set(inserted)

tested = [
    s for s in (random_string() for _ in range(15000))
    if s not in inserted_set
]

rows = []

for m in ms:
    bf = BloomFilter(n, 0.01)

    k = max(1, int(round((m / n) * math.log(2))))

    bf.m = m
    bf.k = k
    bf.bits = bitarray(m)
    bf.bits.setall(False)
    bf.count = 0

    for word in inserted:
        bf.add(word)

    false_positives = sum(1 for word in tested if word in bf)

    measured_fpr = false_positives / len(tested)

    rows.append({
        "m": m,
        "k": k,
        "measured_fpr": measured_fpr
    })

    print(f"m={m} k={k} fpr={measured_fpr:.4f}")

with open("results/experiment_size.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
