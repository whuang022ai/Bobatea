#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sys
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from io import StringIO
import argparse
import pandas as pd
parser = argparse.ArgumentParser(description='sklearn Hierarchical Cluster ')

data = pd.read_csv(sys.stdin, index_col=0,header=0)

X = data.values.T

Y = pdist(X)
Z = linkage(Y)
dendrogram(Z, labels = data.columns, orientation='right' ) #, orientation='right'

output = StringIO()
data.to_csv(output)
plt.tight_layout()
plt.show()