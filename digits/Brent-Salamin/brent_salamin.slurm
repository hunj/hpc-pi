#!/bin/bash  
#SBATCH --mail-user=hxz347@case.edu
#SBATCH --mail-type=ALL                          
#SBATCH -N 10                             
#SBATCH -c 4
#SBATCH --output=stdout150000

cp brent-salamin.py
cd $PFSDIR 
module load python 
python brent-salamin.py