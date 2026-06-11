#!/bin/bash
#SBATCH --job-name=bloom_hash
#SBATCH --time=00:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=2G
#SBATCH --output=slurm-hash-%j.out

cd $SLURM_SUBMIT_DIR
source .venv/bin/activate 2>/dev/null || true
python -m pip install -q -r requirements.txt
python benchmarks/experiment_hash_quality.py
python benchmarks/experiment_hash_correlation.py
python benchmarks/make_plots.py
