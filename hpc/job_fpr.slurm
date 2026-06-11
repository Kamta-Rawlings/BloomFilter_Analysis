#!/bin/bash
#SBATCH --job-name=bloom_fpr
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --output=slurm-fpr-%j.out

cd $SLURM_SUBMIT_DIR
source .venv/bin/activate 2>/dev/null || true
python -m pip install -q -r requirements.txt
python benchmarks/experiment_fpr.py
python benchmarks/experiment_optimal_k.py
python benchmarks/experiment_size.py
python benchmarks/experiment_words.py
