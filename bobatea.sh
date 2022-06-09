#!/usr/bin/env bash

########################## 
#
# Bobatea datatool config
#
########################## 

alias pca=PCA.py
alias log=Log.py
alias take=ColumnTake.py
alias drop=ColumnDrop.py
alias csvf=CSVFilter.py
alias scatter=Scatter.py
alias t=DataT.py
alias pair=PairPlot.py
alias hcluster=HierarchicalCluster.py
alias kmean=Kmeans.py
alias index=CSVAddIndex.py
alias header=CSVAddHeader.py
alias merge=CSVMerge.py
alias tsne=tSNE.py
alias curve=Curve.py
alias mean=ArithmeticMean.py
alias kat=Concatenate.py

range (){
    head -n "$2" | tail -n +"$1"
}