#!/bin/sh
while read target
do
  echo $target
  python3 rakuten.py $target >> ./output/$target.txt 
done < ./list.csv
