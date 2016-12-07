# Pi Computation using CWRU HPCC

Helen Zhao (hxz347), Hun Jae Lee (hxl224)

EECS338 Operating Systems Final Project

Demo due Tuesday, Dec. 6, 2016

## Introduction

Our group have introduced the four mathematical formulas or algorithms for approximating/computing Pi: 

- Ramanujan-Sato series
- Chudnovsky Algorithm
- Brent-Salamin Formula
- Monte-Carlo Method

We have implemented them in Python script and ran SLURM scripts in order to run calculation in parallel manner.
One implementation will be in time constraint, where each calculation runs for given amount of time (in minutes). Another is for digits, where each calculation runs up to certain digits.

## Progress Report

Implement the following in two ways.

- Time:

- [ ] Ramanujan-Sato series 
- [ ] Chudnovsky Algorithm
- [ ] Brent-Salamin Formula
- [ ] Monte-Carlo Method

- Digits:

- [ ] Ramanujan-Sato series 
- [ ] Chudnovsky Algorithm
- [ ] Brent-Salamin Formula
- [ ] Monte-Carlo Method

## How to run

- `make 1min` to run all 4 algorithms
- Running in HPC with SLURM script

## Result

The results are in each directory, `/time/result` and `/digits/result`

## Example of SLURM script

The following is a template for SLURM script, used in order to add a job to HPC:

```shell
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

```

