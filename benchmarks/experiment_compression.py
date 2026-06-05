# experiment_compression.py
# Compare memory: python set vs bloom filter.
import csv, os, sys
from bloomfilter import BloomFilter

SIZES = [1000, 10000, 100000, 500000]
os.makedirs("results", exist_ok=True)
rows = []

for n in SIZES:
    s = set()
    for i in range(n):
        s.add("item-" + str(i))
    set_bytes = sys.getsizeof(s) + sum(sys.getsizeof(x) for x in s)

    bf = BloomFilter(n, 0.01)
    for i in range(n):
        bf.add("item-" + str(i))
    bloom_bytes = bf.m // 8

    rows.append({
        "n": n,
        "set_bytes": set_bytes,
        "bloom_bytes": bloom_bytes,
        "compression_ratio": set_bytes / bloom_bytes,
    })
    print("n=%d  set=%d B  bloom=%d B  ratio=%.1fx" %
          (n, set_bytes, bloom_bytes, set_bytes / bloom_bytes))

with open("results/experiment_compression.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print("wrote results/experiment_compression.csv")
