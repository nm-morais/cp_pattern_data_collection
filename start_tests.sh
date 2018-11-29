#!/bin/bash

#max size of the work
max_src_size=$1

#increment of the size to test
increment_size=$2

#max workers, dont go crazy
max_workers=$3

# times to run a pattern in order to extract an average
times_to_average=$4

if [[ "$#" -ne 4 ]]; then
    echo ""
    echo "INVALID USAGE"
  	echo "USAGE: [MAX SOURCE SIZE] [INCREMENT] [MAX WORKERS] [TIMES TO AVERAGE]"
    echo ""
  	exit 1
fi

rm data/log
echo ""
echo "--------------COMPILING--------------"
cd src 
make
cd ..
echo "--------------DONE--------------"
echo ""
echo "--------------STARTING TESTS--------------"

curr_size=$increment_size;
nWorkers=1
while [[ $nWorkers -le $max_workers ]]; do
	export CILK_NWORKERS=${nWorkers}
 
  while [[ $curr_size -le $max_src_size ]]; do
    echo "STARTING: ./main ${curr_size} ${nWorkers} ${times_to_average}"
    echo "NEW_TEST ${curr_size} ${nWorkers}" >> data/log
  	./src/main $curr_size $nWorkers $times_to_average >> data/log
    ((curr_size=$curr_size+$increment_size))
	done
  curr_size=$increment_size
  ((nWorkers++))
done
echo ""
echo "DONE!"

aux=$((max_src_size / increment_size))

echo ""
echo "PARSING AND MAKING GRAPHS"
echo ""
echo "Starting : data/parser.py ${aux} ${max_workers}" 
rm data/graphs/* &> /dev/null
rm data/csv/* &> /dev/null
mkdir data/graphs &> /dev/null
mkdir data/csv &> /dev/null
python3 data/parser.py $aux $max_workers

echo ""
echo "DONE"
echo ""