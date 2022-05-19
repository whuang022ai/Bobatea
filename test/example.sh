#!/usr/bin/env bash
shopt -s expand_aliases
source ../bobatea.sh

cat iris.data | header --h "sepal_length,sepal_width,petal_length,petal_width,species" |index | cdrop --w "species" | log | pca | scatter > pca.csv
cat pca.csv | kmean > kmean.csv
