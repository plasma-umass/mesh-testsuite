#!/bin/bash
set -euo pipefail

N=3
if [ "$#" -gt 0 ]; then
    N=$1
fi
echo "doing $N runs"


(cd Speedometer && serve &)

cd atsy

i=0
while [ $i -lt $N ]; do
    echo "run $i"
    ./run_speedometer
    i=$[$i+i]
done
