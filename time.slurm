#!/bin/bash
#SBATCH --mail-user=hunj@case.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --output=pi.output

nproc=$(expr $SLURM_JOB_CPUS_PER_NODE \* $SLURM_NNODES)
echo $nproc cores available.

cp -r * $PFSDIR/.
cd $PFSDIR
module load python
mkdir time/result;
python time/pi_monte-carlo.py 1 >> time/result/monte-carlo-1min &
python time/pi_chudnovsky.py 1 >> time/result/chudnovsky-1min &
python time/pi_brent-salamin.py 1 >> time/result/pi_brent-salamin-1min &
python time/pi_ramanujan-sato.py 1 >> time/result/ramanujan_sato-1min