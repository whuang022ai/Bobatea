#!/usr/bin/env bash
shopt -s expand_aliases
source ../bobatea.sh

cat iris.data | header --h "sepal_length,sepal_width,petal_length,petal_width,species" |index > iris.csv
cat iris.csv | cdrop --w "species" | tsne > iris_tsne.csv
cat iris_tsne.csv | scatter

