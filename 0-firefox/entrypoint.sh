#!/bin/bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "usage: ./entrypoint.sh N_RUNS WAIT_TIME" >&2
    exit 1
fi

N=$1
export TEST_WAIT_SECS=$2
echo "doing $N runs"


(cd Speedometer && serve &)

cd atsy

i=0
while [ $i -lt $N ]; do
    echo "run $i"
    ./run_speedometer
    i=$(($i+1))
done
