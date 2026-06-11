# BloomFilter Analysis

## Team Members

- Longkong Rawlings Kamta 240785
- Ihame Gilbert 2504417

---

# Repository Structure

```text
BloomFilter_Analysis/
├── benchmarks/
│   ├── benchmark_ops.py
│   ├── experiment_compression.py
│   ├── experiment_fpr.py
│   ├── experiment_hash_correlation.py
│   ├── experiment_hash_quality.py
│   ├── experiment_hit_vs_miss.py
│   ├── experiment_optimal_k.py
│   ├── experiment_size.py
│   ├── experiment_words.py
│   └── make_plots.py
│
├── bloomfilter/
│   ├── __init__.py
│   ├── bloom.py
│   └── hashing.py
│
├── datasets/
│   └── words.txt
│
├── hpc/
│   ├── hpc_readme.md
│   ├── job_benchmark.slurm
│   ├── job_fpr.slurm
│   ├── job_hashes.slurm
│   └── job_ops.slurm
│
├── notebooks/
│   └── demo.ipynb
│
├── results/
│   ├── *.csv
│   └── *.png
│
├── tests/
│   ├── test_bloom.py
│   ├── test_hashing.py
│   └── __init__.py
│
├── environment.yml
├── pyproject.toml
├── README.md
└── .gitignore
```

---

# Project Description

This project implements a Bloom Filter, a probabilistic data structure used for efficient membership testing. Bloom filters provide:

* Fast insertion
* Fast lookup
* No false negatives
* Small memory footprint

False positives are possible and are studied experimentally throughout the project.

---

# Implementation

## bloomfilter/bloom.py

Contains the main BloomFilter implementation.

Features include:

* Automatic computation of optimal filter size (m)
* Automatic computation of optimal number of hash functions (k)
* Item insertion
* Membership testing
* False positive rate estimation
* Memory usage analysis

---

## bloomfilter/hashing.py

Contains the hashing utilities used by the Bloom filter.

Implemented hash functions include:

* Blake2b (default)
* DJB2
* SDBM
* FNV-1a

The project uses Kirsch-Mitzenmacher double hashing to generate multiple Bloom filter positions efficiently.

---

# Test Suite

The test suite verifies:

* Inserted items are always found
* No false negatives occur
* False positive rate remains reasonable
* Hash positions remain within valid ranges
* Hash functions are deterministic
* Different inputs generate different positions
* Invalid constructor parameters raise exceptions

Run the tests using:

```bash
pytest -v
```

---

# Benchmarks and Experiments

The project contains several experiments used to analyze Bloom filter behaviour.

## experiment_fpr.py

Measures the false positive rate as the number of inserted elements increases.

Produces:

* experiment_fpr.csv
* fpr_vs_load.png

---

## experiment_size.py

Measures how false positive rate changes with Bloom filter size.

Produces:

* experiment_size.csv

---

## experiment_optimal_k.py

Studies the impact of the number of hash functions.

Produces:

* experiment_optimal_k.csv
* optimal_k.png

---

## experiment_compression.py

Compares Bloom filter memory usage against a Python set.

Produces:

* experiment_compression.csv
* compression.png

---

## experiment_hit_vs_miss.py

Compares lookup time for present and absent items.

Produces:

* experiment_hit_vs_miss.csv
* hit_vs_miss.png

---

## experiment_hash_quality.py

Evaluates the distribution quality of different hash functions.

Produces:

* Histogram CSV files
* Histogram PNG plots

---

## experiment_hash_correlation.py

Studies correlation between pairs of hash functions.

Produces:

* Correlation CSV files
* Correlation scatter plots

---

## experiment_words.py

Evaluates Bloom filter behaviour using a real English-word dataset.

Produces:

* experiment_words.csv
* words_fpr.png

---

## benchmark_ops.py

Measures insertion and lookup performance.

Produces:

* benchmark_ops.csv
* ops_time.png

---

# Running the Project

Create the environment:

```bash
conda env create -f environment.yml
conda activate bloomfilter_analysis
```

Run tests:

```bash
pytest -v
```

---

# Running Experiments

Examples:

```bash
python -m benchmarks.experiment_fpr
python -m benchmarks.experiment_optimal_k
python -m benchmarks.experiment_compression
python -m benchmarks.benchmark_ops
```

Generate all plots:

```bash
python -m benchmarks.make_plots
```

---

# HPC Execution

The project was tested on the KU Leuven HPC infrastructure.

The `hpc/` directory contains:

* SLURM job scripts
* HPC-specific environment file

Example:

```bash
sbatch hpc/job_fpr.slurm
```

Monitor jobs:

```bash
squeue -u $USER
```

---

# Main Findings

The experiments confirm several theoretical Bloom filter properties:

1. The measured false positive rate closely matches the theoretical false positive rate.

2. Increasing filter size significantly reduces false positives.

3. An optimal number of hash functions exists that minimizes false positive rate.

4. Bloom filters provide substantial memory savings compared to storing all items in a Python set.

5. Lookup operations for present and absent elements have nearly identical execution times.

6. The implemented hash functions exhibit good distribution and low correlation.

These results demonstrate that Bloom filters are highly efficient for large-scale membership testing where small false positive rates are acceptable.
