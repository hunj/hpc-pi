#!/bin/bash
#SBATCH --mail-user=hunj@case.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --output=pi.output

nproc=$(expr $SLURM_JOB_CPUS_PER_NODE \* $SLURM_NNODES)
echo $nproc cores available.

cp *.py $PFSDIR/.
cd $PFSDIR
module load python
# python pi_monte-carlo.py 36000