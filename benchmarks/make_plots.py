# Make the PNG plots from the CSVs in results/
import csv
import os

import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)


def load(path):
    with open(path) as f:
        return list(csv.DictReader(f))

# ops timing
ops = load("results/benchmark_ops.csv")

ns = [int(r["n"]) for r in ops]
add_us = [float(r["add_us_per_op"]) for r in ops]
look_us = [float(r["lookup_us_per_op"]) for r in ops]

plt.figure()
plt.plot(ns, add_us, "o-", label="add")
plt.plot(ns, look_us, "s-", label="lookup")
plt.xscale("log")
plt.xlabel("n items")
plt.ylabel("us / op")
plt.title("time per operation")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("results/ops_time.png", dpi=120, bbox_inches="tight")
plt.close()