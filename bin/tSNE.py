#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse
from sklearn import manifold
parser = argparse.ArgumentParser(description='sklearn tSNE ')
parser.add_argument('-n','--n_components', action='store', dest='n_components',
                    default=2 ,help='set tSNE output component number' )
parser.add_argument('-t','--transform', action='store_true',
                    dest='input_matrix_transform',
                    help='input matrix transform (input.T)')

args = parser.parse_args()

data = pd.read_csv(sys.stdin, index_col=0)

if args.input_matrix_transform:
    X = data.values.T
    index_out = data.columns
else:
    X = data.values
    index_out = data.index

tSNE = manifold.TSNE(n_components=int(args.n_components))

X_tSNE = tSNE.fit_transform(X)
output = StringIO()
new_column = ['tSNE' + str(i + 1) for i in range(X_tSNE.shape[1])]
pd.DataFrame(X_tSNE, index=index_out, columns=new_column).to_csv(output,
        header=True, index=True)
print (output.getvalue(), file = sys.stdout)
