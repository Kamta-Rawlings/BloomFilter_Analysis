#!/bin/bash
# SLURM job script for running the benchmarks on the VSC HPC.
# Submit with:  sbatch hpc/job_benchmark.slurm

#SBATCH --job-name=bloom_bench
#SBATCH --output=results/slurm_%j.out
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G

# Load conda + activate the env
module load Miniconda3
source activate bloomfilter_analysis

# Run the three experiments and then make the plots
python benchmarks/benchmark_ops.py
python benchmarks/experiment_fpr.py
python benchmarks/experiment_compression.py
python benchmarks/make_plots.py
