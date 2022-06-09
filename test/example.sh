#!/usr/bin/env bash
shopt -s expand_aliases
source ../bobatea.sh

cat iris.data | header --h "sepal_length,sepal_width,petal_length,petal_width,species"  | drop species | pca | scatter -t "Iris Data" -x "PC1" -y "PC2" -img "ex1.png" > pca.csv
cat pca.csv | kmean  > kmean.csv
cat pca.csv  | tsne  | scatter 
