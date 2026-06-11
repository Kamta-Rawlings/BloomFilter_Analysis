# Running on the KU Leuven HPC

This project was developed and tested on the KU Leuven HPC infrastructure.

## 1. Login to the HPC

Open:

https://ondemand.hpc.kuleuven.be/

and login using your KU Leuven/VSC credentials.

After logging in, open:

```text
Interactive Shell
```

from the Open OnDemand dashboard.

---

## 2. Clone the Repository

Inside the interactive shell:

```bash
git clone <repository-url>
cd BloomFilter_Analysis
```

Example:

```bash
git clone https://github.com/username/BloomFilter_Analysis.git
cd BloomFilter_Analysis
```

---

## 3. Load Miniconda

The KU Leuven HPC provides Miniconda as a module.

Load the required modules:

```bash
module load cluster/genius/login
module load Miniconda3/4.12.0
```

Verify that conda is available:

```bash
conda --version
```

---

## 4. Create the Conda Environment

Create the project environment from the provided environment file:

```bash
conda env create -f environment.yml
```

This only needs to be done once.

---

## 5. Activate the Environment

On the HPC, Conda activation requires initializing the shell first:

```bash
source $(conda info --base)/etc/profile.d/conda.sh
conda activate bloomfilter_analysis
```

Verify:

```bash
which python
python --version
```

---

## 6. Run the Test Suite

Before running experiments, verify that everything works:

```bash
pytest -v
```

Expected output:

```text
10 passed
```

---

## 7. Run the Experiments

All benchmark scripts should be executed as Python modules from the repository root.

### False Positive Rate

```bash
python -m benchmarks.experiment_fpr
```

### Bloom Filter Size

```bash
python -m benchmarks.experiment_size
```

### Optimal Number of Hash Functions

```bash
python -m benchmarks.experiment_optimal_k
```

### Compression Analysis

```bash
python -m benchmarks.experiment_compression
```

### Hit vs Miss Lookup Time

```bash
python -m benchmarks.experiment_hit_vs_miss
```

### Hash Quality

```bash
python -m benchmarks.experiment_hash_quality
```

### Hash Correlation

```bash
python -m benchmarks.experiment_hash_correlation
```

### Real Words Dataset

```bash
python -m benchmarks.experiment_words
```

### Performance Benchmark

```bash
python -m benchmarks.benchmark_ops
```

---

## 8. Generate Plots

After all experiments have completed:

```bash
python -m benchmarks.make_plots
```

This generates all PNG visualizations from the CSV files.

---

## 9. View Results

All generated files are stored in:

```text
results/
```

This directory contains:

* CSV files with raw measurements
* PNG plots generated from the measurements

Example:

```bash
ls results
```

---

## 10. Save Results to GitHub

After generating the results, commit them to the repository:

```bash
git add results/
git commit -m "Add benchmark results generated on HPC"
git push
```

This uploads all generated CSV files and plots to GitHub.

---

## HPC Workflow Summary

```bash
module load cluster/genius/login
module load Miniconda3/4.12.0

conda env create -f environment.yml

source $(conda info --base)/etc/profile.d/conda.sh
conda activate bloomfilter_analysis

pytest -v

python -m benchmarks.experiment_fpr
python -m benchmarks.experiment_size
python -m benchmarks.experiment_optimal_k
python -m benchmarks.experiment_compression
python -m benchmarks.experiment_hit_vs_miss
python -m benchmarks.experiment_hash_quality
python -m benchmarks.experiment_hash_correlation
python -m benchmarks.experiment_words
python -m benchmarks.benchmark_ops

python -m benchmarks.make_plots

git add results/
git commit -m "Add benchmark results generated on HPC"
git push
```
