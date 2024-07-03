#!/bin/bash
#SBATCH --qos=cbmm
#SBATCH -p cbmm
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=08:00:00
#SBATCH --output=./jupyter/log_jupyter.sh

hostname

unset XDG_RUNTIME_DIR

source ~/.bashrc
source activate pytorch

jupyter lab --ip=0.0.0.0 --port=9324 --no-browser

## ssh -L 8888:localhost:9324 galanti@openmind.mit.edu
## In the browser, use: http://localhost:8888/lab