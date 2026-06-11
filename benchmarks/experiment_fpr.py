# experiment_fpr.py
# Fill the filter step by step and measure FPR.

import csv
import os
from bloomfilter import BloomFilter

CAP = 10000
P = 0.01
STEPS = 20
Q = 5000   # queries per step


os.makedirs("results", exist_ok=True)

bf = BloomFilter(CAP, P)
rows = []

for step in range(1, STEPS + 1):
    start = (step - 1) * (CAP // STEPS)
    end = step * (CAP // STEPS)
    for i in range(start, end):
        bf.add("in-" + str(i))

    fp = 0
    for i in range(Q):
        if ("never-%d-%d" % (step, i)) in bf:
            fp += 1
    measured = fp / Q

    rows.append({
        "items_inserted": end,
        "load_factor": end / CAP,
        "fill_ratio": bf.fill_ratio(),
        "theoretical_fpr": bf.estimated_fpr(),
        "measured_fpr": measured,
    })
    print("n=%d  measured=%.4f  theory=%.4f" % (end, measured, bf.estimated_fpr()))

with open("results/experiment_fpr.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print("wrote results/experiment_fpr.csv")
