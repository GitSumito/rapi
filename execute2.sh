#!/bin/sh
while read target
do
  echo $target
  python rakuten.py $target > ./output/$target.txt 
done < ./list.csv
