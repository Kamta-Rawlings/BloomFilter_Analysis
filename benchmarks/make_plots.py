# Make the PNG plots from the CSVs in results/
import csv
import os
import glob

import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)


def load(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def col(rows, k, cast=float):
    return [cast(r[k]) for r in rows]

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

# optimal k
if os.path.exists("results/experiment_optimal_k.csv"):
    ok = load("results/experiment_optimal_k.csv")

    plt.figure()
    plt.plot(col(ok, "k", int), col(ok, "measured_fpr"), "o-", label="measured")
    plt.plot(col(ok, "k", int), col(ok, "theoretical_fpr"), "--", label="theory")

    plt.xlabel("k (number of hashes)")
    plt.ylabel("false positive rate")
    plt.title("FPR vs k")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig("results/optimal_k.png", dpi=120, bbox_inches="tight")
    plt.close()


# FPR vs size m
if os.path.exists("results/experiment_size.csv"):
    sz = load("results/experiment_size.csv")

    plt.figure()
    plt.plot(col(sz, "m", int), col(sz, "measured_fpr"), "o-")

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("filter size m (bits)")
    plt.ylabel("false positive rate")
    plt.title("FPR vs filter size")

    plt.grid(True, alpha=0.3)

    plt.savefig("results/fpr_vs_size.png", dpi=120, bbox_inches="tight")
    plt.close()


# histogram per hash function
for path in sorted(glob.glob("results/hist_*.csv")):
    name = os.path.basename(path)[5:-4]

    rows = load(path)

    buckets = col(rows, "bucket", int)
    counts = col(rows, "count", int)

    plt.figure()
    plt.bar(buckets, counts)

    plt.xlabel("bucket")
    plt.ylabel("count")
    plt.title(f"Hash distribution: {name}")

    plt.grid(True, alpha=0.3, axis="y")

    plt.savefig(f"results/hist_{name}.png",
                dpi=120,
                bbox_inches="tight")
    plt.close()


# hash correlation plots
for path in sorted(glob.glob("results/corr_*.csv")):
    label = os.path.basename(path)[5:-4]

    rows = load(path)

    xs = col(rows, "x", int)
    ys = col(rows, "y", int)

    plt.figure()
    plt.scatter(xs, ys, s=4, alpha=0.5)

    plt.xlabel("hash A mod M")
    plt.ylabel("hash B mod M")
    plt.title(f"Correlation: {label}")

    plt.grid(True, alpha=0.3)

    plt.savefig(f"results/corr_{label}.png",
                dpi=120,
                bbox_inches="tight")
    plt.close()


# real words FPR
if os.path.exists("results/experiment_words.csv"):
    ww = load("results/experiment_words.csv")

    plt.figure()

    xs = list(range(len(ww)))
    labels = [r["target_fpr"] for r in ww]

    plt.bar(
        [x - 0.2 for x in xs],
        col(ww, "target_fpr"),
        width=0.4,
        label="target"
    )

    plt.bar(
        [x + 0.2 for x in xs],
        col(ww, "measured_fpr"),
        width=0.4,
        label="measured"
    )

    plt.yscale("log")
    plt.xticks(xs, labels)

    plt.xlabel("target FPR")
    plt.ylabel("FPR (log)")
    plt.title("Real English Words: Target vs Measured FPR")

    plt.legend()
    plt.grid(True, alpha=0.3, axis="y")

    plt.savefig("results/words_fpr.png",
                dpi=120,
                bbox_inches="tight")
    plt.close()


# hit vs miss lookup time
if os.path.exists("results/experiment_hit_vs_miss.csv"):
    hm = load("results/experiment_hit_vs_miss.csv")

    plt.figure()

    plt.plot(
        col(hm, "n", int),
        col(hm, "hit_us"),
        "o-",
        label="hit"
    )

    plt.plot(
        col(hm, "n", int),
        col(hm, "miss_us"),
        "s-",
        label="miss"
    )

    plt.xscale("log")

    plt.xlabel("n")
    plt.ylabel("us / lookup")

    plt.title("Lookup Time: Hit vs Miss")

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig("results/hit_vs_miss.png",
                dpi=120,
                bbox_inches="tight")
    plt.close()

print("all plots done")
