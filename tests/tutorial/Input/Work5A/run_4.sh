#!/bin/bash -x
(cd ../../../../tmp/; make mj4)
mpirun -n 4 time abinit < t03_x.files  > log 2> err
#mpirun -n 4 time abinit < t03_x.files > log 2> err  | tail -f log  | grep -e ETOT 

