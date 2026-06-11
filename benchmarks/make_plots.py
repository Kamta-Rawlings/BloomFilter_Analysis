# Make the PNG plots from the CSVs in results/
import csv
import os

import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)


def load(path):
    with open(path) as f:
        return list(csv.DictReader(f))