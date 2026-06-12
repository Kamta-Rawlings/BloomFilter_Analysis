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

# Complexity Analysis

Let:

* **m** be the number of bits in the Bloom filter.
* **k** be the number of hash functions.
* **n** be the number of inserted elements.

### Insertion

To insert an item, the Bloom filter computes **k** hash positions and sets **k** bits in the bit array.

Time complexity:

```text
O(k)
```

Since k is typically small and fixed, insertion is effectively constant time.

### Membership Query

To test whether an item is present, the Bloom filter computes the same **k** hash positions and checks the corresponding bits.

Time complexity:

```text
O(k)
```

As with insertion, k is usually small and fixed.

### Space Complexity

The Bloom filter stores a bit array of size **m** bits.

Space complexity:

```text
O(m)
```

The memory usage depends only on the filter size and not on the number of inserted elements after construction.

### Hashing Complexity

For an input string of length **L**, hashing requires processing each character.

Hashing complexity:

```text
O(L)
```

For bounded-length strings, the overall insertion and lookup operations remain approximately O(k).

### Experimental Verification

The benchmark experiments (`benchmark_ops.py`) show that insertion and lookup times remain nearly constant as the number of stored elements increases, confirming the expected theoretical complexity.


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

Evaluates the distribution quality of different hash functions on both natural-language words and randomly generated strings.

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

## Hash Function Validation

The hash functions were evaluated using two different data types:

- Natural language words (`datasets/words.txt`)
- Randomly generated strings created during the experiments

For both datasets, histogram and correlation experiments were performed to evaluate:

- Distribution uniformity
- Bucket occupancy
- Correlation between hash functions

The results indicate that the implemented hash functions distribute values approximately uniformly and exhibit low correlation on both datasets, making them suitable for Bloom filter applications.

---

## datasets/

Contains datasets used during testing and experimentation.

Files:

* words.txt – a collection of English words used to evaluate false positive rates and hash function behaviour.
* random_strings.txt – randomly generated strings used to test the robustness and distribution quality of the hash functions on a different type of data.

---

## results/

Contains all output generated by the experiments.

Files include:

* CSV files containing raw benchmark and experiment results.
* PNG files containing plots generated from the CSV results.

Examples:

* benchmark_ops.csv
* experiment_fpr.csv
* compression.png
* ops_time.png
* optimal_k.png

These files are generated automatically by the benchmark scripts and are used to analyse Bloom filter performance.

---

## tests/

Contains automated unit tests for the project.

The tests verify:

* Correct insertion behaviour.
* Correct membership queries.
* Absence of false negatives.
* Hash function correctness.
* Parameter validation.
* Expected Bloom filter properties.

---

## hpc/

Contains files required to execute experiments on the KU Leuven HPC infrastructure.

Files:

* hpc_readme.md – instructions for running the project on the HPC.
* job_benchmark.slurm – SLURM script for running benchmark experiments.
* job_fpr.slurm – SLURM script for false positive rate experiments.
* job_hashes.slurm – SLURM script for hash function experiments.
* job_ops.slurm – SLURM script for insertion and lookup timing experiments.

These scripts were used to perform large-scale experiments on the HPC cluster.

---

## environment.yml

Defines the Conda environment required to run the project.

The file specifies:

* Python version.
* Required scientific libraries.
* Bloom filter dependencies.
* Testing dependencies.

---

## pyproject.toml

Project configuration file used by Python tooling.

It contains metadata and configuration information required for packaging, testing, and project management.

---

## notebooks/

Contains Jupyter notebooks used for demonstration and interactive exploration.

Files:

* demo.ipynb – demonstrates how to create a Bloom filter, insert elements, perform membership queries, and inspect Bloom filter behaviour.

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

* The measured false positive rate closely matches the theoretical false positive rate predicted by Bloom filter theory.

* Increasing the filter size significantly reduces the false positive rate, while overloading the filter beyond its design capacity increases the probability of false positives.

* An optimal number of hash functions exists that minimizes the false positive rate for a given filter size.

* Bloom filters provide substantial memory savings compared to storing all elements explicitly in a Python set, while maintaining fast membership queries.

* Insert and lookup operations remain approximately constant-time with respect to the number of stored elements, confirming the expected O(k) complexity.

* Lookup operations for present and absent elements have very similar execution times.

* The implemented hash functions (Blake2b, DJB2, SDBM, and FNV-1a) exhibit good distribution and low correlation.

* Hash quality was evaluated using both natural-language words and randomly generated strings, demonstrating that the hash functions perform well across different data types.

These results demonstrate that Bloom filters are highly efficient for large-scale membership testing where small false positive rates are acceptable and memory efficiency is important.

