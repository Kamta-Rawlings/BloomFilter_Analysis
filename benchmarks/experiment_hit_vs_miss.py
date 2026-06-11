# experiment_hit_vs_miss.py
# Compare lookup times for items that are in the filter (hits)
# and items that are not in the filter (misses).

import csv
import os
import random
import string
import time

from bloomfilter import BloomFilter

os.makedirs("results", exist_ok=True)
random.seed(5)


def random_string():
    return "".join(random.choices(string.ascii_letters, k=10))


sizes = [10000, 50000, 100000, 250000]
rows = []

for n in sizes:

    # Generate inserted and non-inserted items
    inserted = [random_string() for _ in range(n)]
    missing = [random_string() for _ in range(n)]

    bf = BloomFilter(n, 0.01)

    # Fill the Bloom filter
    for word in inserted:
        bf.add(word)

    # Measure hit lookup time
    start = time.perf_counter()
    for word in inserted:
        _ = word in bf
    hit_time = (time.perf_counter() - start) / n * 1e6

    # Measure miss lookup time
    start = time.perf_counter()
    for word in missing:
        _ = word in bf
    miss_time = (time.perf_counter() - start) / n * 1e6

    rows.append({
        "n": n,
        "hit_us": hit_time,
        "miss_us": miss_time
    })

    print(
        "n=%d hit=%.2f us miss=%.2f us"
        % (n, hit_time, miss_time)
    )

# Save results
with open("results/experiment_hit_vs_miss.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=list(rows[0].keys())
    )
    writer.writeheader()
    writer.writerows(rows)
