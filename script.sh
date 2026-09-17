#!/bin/bash
echo "введите число N:"
read N
for i in $(seq 1 $N)
do
	touch "file$i.txt"
     x=$RANDOM
     y=$RANDOM
     z=$(($x+$y))
     echo "$z">file$i.txt
     cat file$i.txt
done
