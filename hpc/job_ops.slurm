#!/bin/bash
#SBATCH --job-name=bloom_ops
#SBATCH --time=00:20:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --output=slurm-ops-%j.out

cd $SLURM_SUBMIT_DIR
source .venv/bin/activate 2>/dev/null || true
python -m pip install -q -r requirements.txt
python benchmarks/benchmark_ops.py
python benchmarks/experiment_compression.py
python benchmarks/experiment_hit_vs_miss.py
