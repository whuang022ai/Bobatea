#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import argparse
import sys
import seaborn as sns
parser = argparse.ArgumentParser(description='sklearn Kmeans ')
parser.add_argument('--n', action='store', dest='n_clusters',
                    default=3)
args = parser.parse_args()
data = pd.read_csv(sys.stdin, index_col=0)


model = KMeans(init='k-means++', n_clusters=int(args.n_clusters), n_init=int(args.n_clusters)*3)
model.fit(data)

data['kmeans_predicted_cluster'] = model.labels_.astype(int)
output = StringIO()
data.to_csv(output)

print (output.getvalue())

ax=sns.scatterplot(x=data.columns[0], y=data.columns[1], hue="kmeans_predicted_cluster", data=data)

for i, marker in enumerate(data.index):
    ax.annotate(marker, (data.values[i, 0], data.values[i, 1] ), fontsize=6)

plt.show()