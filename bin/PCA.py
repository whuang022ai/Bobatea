#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.decomposition import PCA
import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse

parser = argparse.ArgumentParser(description='sklearn PCA ')
parser.add_argument('--n', action='store', dest='n_components',
                    default=2)
parser.add_argument('--t', action='store_true',
                    dest='input_matrix_transform',
                    help='input matrix transform (input.T)')
parser.add_argument('--expr', action='store',
                    dest='explained_variance_ratio_outputpath')
args = parser.parse_args()

data = pd.read_csv(sys.stdin, index_col=0)

if args.input_matrix_transform:
    X = data.values.T
    index_out = data.columns
else:
    X = data.values
    index_out = data.index

pca = PCA(n_components=int(args.n_components))

X_pca = pca.fit_transform(X)
output = StringIO()
new_column = ['PC' + str(i + 1) for i in range(X_pca.shape[1])]
pd.DataFrame(X_pca, index=index_out, columns=new_column).to_csv(output,
        header=True, index=True)
print (output.getvalue())

if args.explained_variance_ratio_outputpath:
    np.savetxt(args.explained_variance_ratio_outputpath,
               pca.explained_variance_ratio_ * 100, delimiter=',',
               fmt='%f')
