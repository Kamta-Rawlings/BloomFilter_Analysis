# benchmark_ops.py
# Times add() and contains() for different n. Writes a CSV.
import csv, time, os
from bloomfilter import BloomFilter

SIZES = [1000, 10000, 100000, 500000]

os.makedirs("results", exist_ok=True)

rows = []

for n in SIZES:
    bf = BloomFilter(n, 0.01)

    t0 = time.perf_counter()
    for i in range(n):
        bf.add("item-" + str(i))
    t_add = time.perf_counter() - t0

    t0 = time.perf_counter()
    for i in range(n):
        _ = "item-" + str(i) in bf
    t_look = time.perf_counter() - t0

    rows.append({
        "n": n,
        "add_total_s": t_add,
        "lookup_total_s": t_look,
        "add_us_per_op": t_add / n * 1e6,
        "lookup_us_per_op": t_look / n * 1e6,
    })

    print("n=%d  add=%.3fs  lookup=%.3fs" % (n, t_add, t_look))

with open("results/benchmark_ops.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print("wrote results/benchmark_ops.csv")
