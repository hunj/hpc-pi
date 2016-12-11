#!/bin/bash 
#SBATCH --mail-user=hxz347@case.edu
#SBATCH --mail-type=ALL  
#SBATCH -N 10
#SBATCH -c 4
#SBATCH --output= 5digits.std 

cp pi_ramanujan-sato.py $PFSDIR/.
cd $PFSDIR
module load python
python pi_ramanujan-sato.py 2000