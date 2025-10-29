#!/usr/bin/python
from __future__ import print_function
import numpy as np
import os,sys
from ase import Atoms
from ase.data import covalent_radii
from ase.visualize import view
from ase.calculators.neighborlist import *
from ase.io import read
import pandas as pd
#================================================
def find_cluster(atom_index):
  pool= set([])
  diff= set([atom_index])
  while diff != set([]):
    new=[]
    for i in list(diff):
      new = new + nl.get_neighbors(i)[0].tolist()
  
    newpool= pool | set (new)
    diff   = newpool - pool
    pool = newpool
#    print diff
  return pool
#================================================

fin=   str(sys.argv[1])
structures = read(fin,':')

df=pd.read_csv(sys.argv[2],sep="\s+", usecols=[1,3],names=['steps','temperature'])
ws = df['steps'].to_list()
ws.append(2020000)
ws=np.diff(ws)



 
rcut=4.2
spec_A='Li'
spec_B='Tc'
species=[spec_A,spec_B]


structure=structures[0]

N_spec=len(structure[structure.symbols == spec_A])
hist=[0.0]*N_spec
N=0


for structure,w in zip(structures,ws):
    N += 1
    mask=[False]*len(structure)
    for spec in species:
        mask += structure.symbols == spec

    structure = structure[mask]
    
    

    nl= NeighborList([rcut/2.0]*len(structure),skin=0, self_interaction=True,bothways=True)
    nl.update(structure)
    
    
    
    todo= set(range(len(structure)))
    while todo != set([]):
      cluster= find_cluster(list(todo)[0])
      cluster_atoms=structure[list(cluster)]
      mask_A= cluster_atoms.symbols == spec_A
      size= len(cluster_atoms[mask_A])
      if size > 0:
          hist[ size-1] += w    
      todo= todo - cluster
      

print(f'# SIZE: {N_spec} , IMAGES: {N} ')
for i,h in enumerate(hist):
    print(i+1,h,h*(i+1)/(sum(ws)*N_spec) )
