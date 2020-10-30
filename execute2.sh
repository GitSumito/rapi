#!/bin/sh
while read target
do
  :> ./output/result.txt
  python rakuten.py $target >> ./output/result.txt
done < ./list.csv
