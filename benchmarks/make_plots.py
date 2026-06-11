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

# fpr
fpr = load("results/experiment_fpr.csv")

load_f = [float(r["load_factor"]) for r in fpr]
meas = [float(r["measured_fpr"]) for r in fpr]
theo = [float(r["theoretical_fpr"]) for r in fpr]

plt.figure()
plt.plot(load_f, meas, "o-", label="measured")
plt.plot(load_f, theo, "--", label="theory")
plt.xlabel("load factor")
plt.ylabel("false positive rate")
plt.title("FPR vs load")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("results/fpr_vs_load.png", dpi=120, bbox_inches="tight")
plt.close()

# compression
comp = load("results/experiment_compression.csv")

ns2 = [int(r["n"]) for r in comp]
sb = [int(r["set_bytes"]) for r in comp]
bb = [int(r["bloom_bytes"]) for r in comp]

plt.figure()
plt.plot(ns2, sb, "o-", label="set")
plt.plot(ns2, bb, "s-", label="bloom (1% fpr)")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("n items")
plt.ylabel("bytes")
plt.title("memory: set vs bloom")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("results/compression.png", dpi=120, bbox_inches="tight")
plt.close()
