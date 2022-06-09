#!/usr/bin/env bash
shopt -s expand_aliases
source ../bobatea.sh

cat iris.data | header --h "sepal_length,sepal_width,petal_length,petal_width,species" > iris.csv 
cat iris.csv | drop species | pca > pca2.csv
merge -1 iris.csv -2 pca2.csv > iris_pca.csv

