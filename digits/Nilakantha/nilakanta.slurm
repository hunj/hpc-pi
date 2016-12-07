#!/bin/bash 
#SBATCH --mail-user=hxz347@case.edu
#SBATCH --mail-type=ALL
#SBATCH -N 10
#SBATCH -c 4
#SBATCH --output=1000digits.std

cp pi_nilakantha.py $PFSDIR/.
cd $PFSDIR
module load python
python pi_nilakanta.py