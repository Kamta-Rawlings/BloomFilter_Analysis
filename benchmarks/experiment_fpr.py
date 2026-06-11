# experiment_fpr.py
# Fill the filter step by step and measure FPR.

import csv
import os
from bloomfilter import BloomFilter

CAP = 10000
P = 0.01
STEPS = 20
Q = 5000

os.makedirs("results", exist_ok=True)

bf = BloomFilter(CAP, P)
rows = []
