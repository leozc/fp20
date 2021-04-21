#!/bin/bash -l

# SLURM SUBMIT SCRIPT
#SBATCH --nodes=2
#SBATCH --gres=gpu:2
#SBATCH --ntasks-per-node=2
#SBATCH --mem=0
#SBATCH --time=0-02:00:00

# activate conda env
source activate $1

# -------------------------
# debugging flags (optional)
 export NCCL_DEBUG=INFO
 export PYTHONFAULTHANDLER=1

# on your cluster you might need these:
# set the network interface
# export NCCL_SOCKET_IFNAME=^docker0,lo

# might need the latest cuda
# module load NCCL/2.4.7-1-cuda.10.0
# -------------------------

# run script from above
srun python3 simple_image_classifier.py \
  --trainer.accelerator 'ddp' \
  --trainer.gpus 2 \
  --trainer.num_nodes 2 \
  --trainer.max_epochs 5
