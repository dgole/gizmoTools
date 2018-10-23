import numpy as np
import h5py as h5py
import os.path
import readsnap
from matplotlib import pyplot as plt
import yt
import os
import sys

id = str(sys.argv[1])

inDir      = '/home/dgole/research/gizmo/' + id + '/output/'
outDirBase = '/home/dgole/research/gizmo/' + id + '_plots/'
if not os.path.exists(outDirBase): os.makedirs(outDirBase)
ptype = 0
tsMin = 0
tsMax = 500
nTot  = tsMax-tsMin + 1

def getTimeStepString(n):
    if   n<10 : return '00' + str(n);
    elif n<100: return '0'  + str(n);
    else      : return str(n);

for ts in range(tsMin, tsMax + 1):
    snapName = inDir + 'snapshot_' + getTimeStepString(ts) + '.hdf5'
    ds = yt.load(snapName)
    print(ds.field_list)
    quantity = 'density'
    #p = yt.ParticlePlot(ds, 'particle_position_x', 'particle_position_y', quantity, width=(1.0, 1.0))
    p = yt.ParticlePlot(ds, 'particle_position_x', 'particle_position_y', quantity)
    p.set_xlabel('x')
    p.set_ylabel('y')
    p.zoom(1.8)
    p.set_cmap(quantity, 'viridis')
    #p.set_zlim(quantity, 1.e-22, 1.e-20)
    #save result
    thisOutDir = outDirBase+quantity+'/'
    if not os.path.exists(thisOutDir): os.makedirs(thisOutDir)
    plotName = quantity + '_' + str(ts) + '.png'
    p.save(name=thisOutDir+plotName)




















#
