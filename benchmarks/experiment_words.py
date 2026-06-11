# experiment_words.py
# Evaluate the Bloom filter using a real English word list.

import csv
import os
import random

from bloomfilter import BloomFilter

os.makedirs("results", exist_ok=True)

random.seed(4)

# Load and shuffle words
with open("datasets/words.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

random.shuffle(words)

# Insert half the words, query the other half
half = len(words) // 2
inserted = words[:half]
queried = words[half:]

rows = []

for p in [0.1, 0.05, 0.01, 0.001]:
    bf = BloomFilter(len(inserted), p)

    for word in inserted:
        bf.add(word)

    false_positives = sum(1 for word in queried if word in bf)

    measured_fpr = false_positives / len(queried)

    rows.append({
        "target_fpr": p,
        "measured_fpr": measured_fpr,
        "m": bf.m,
        "k": bf.k
    })

    print(f"target={p:g} measured={measured_fpr:g}")

with open("results/experiment_words.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
