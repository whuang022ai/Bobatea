#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.preprocessing import FunctionTransformer
import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse

def log_transform(x):
    return np.log(x + 1)

log_transformer = FunctionTransformer(log_transform)    

data = pd.read_csv(sys.stdin, index_col=0)

log_data=log_transformer.fit_transform(data)

log_data.fillna(0)
log_data = log_data[ np.isfinite( log_data ).all( axis = 1) ]

output = StringIO()

log_data.to_csv(output, header=True, index=True)
print (output.getvalue())