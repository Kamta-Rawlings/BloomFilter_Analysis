import csv, os, sys
from bloomfilter import BloomFilter

SIZES = [1000, 10000, 100000, 500000]

os.makedirs("results", exist_ok=True)

rows = []