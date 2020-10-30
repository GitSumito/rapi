#!/bin/sh
while read target
do
  echo $target
  :> ./output/result.txt
  python3 rakuten.py $target >> ./output/result.txt 
done < ./list.csv
