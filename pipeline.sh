#!/bin/bash
#
# Submit job
#SBATCH -p dl
#SBATCH -N 1
#SBATCH --gres=gpu:1
#SBATCH -n 8
#SBATCH --job-name=test
#SBATCH --output=res.txt
#
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=100

module purge

module load cuda/11.1

srun hostname
srun sleep 60 