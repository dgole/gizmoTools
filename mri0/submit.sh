#!/bin/bash


#----------------------------------------------------
# Generic SLURM script -- MPI Hello World
#
# This script requests 2 nodes and all 16 cores/node
# for a total of 32 MPI tasks.
#----------------------------------------------------
#SBATCH -J gizmoTesting          # Job name
#SBATCH -o gizmo.%j.out   # stdout; %j expands to jobid
#SBATCH -e gizmo.%j.err   # stderr; skip to combine stdout and stderr
#SBATCH -p development    # queue
#SBATCH -N 2              # Number of nodes, not cores (16 cores/node)
#SBATCH -n 32             # Total number of MPI tasks (if omitted, n=N)
#SBATCH -t 01:00:00       # max time
##SBATCH -A AB-01234      # class project/account code;
                          # necessary if you have multiple project accounts

#--------------------------------------------------
#module restore system
module load intel mvapich2 gsl hdf5 fftw2
#cd ./gizmo-public
#make         

ibrun tacc_affinity ./GIZMO ./mri.params 1>gizmo.out 2>gizmo.err  





