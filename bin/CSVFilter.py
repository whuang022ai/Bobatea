#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import numpy as np
from io import StringIO
import argparse

parser = argparse.ArgumentParser(description='csv/tsv/txt dataframe filter ')

dic={'csv':',','tsv':'\t','txt':' '}

parser.add_argument('--d', action='store', dest='decimal',
                    default="csv")

parser.add_argument('--c', action='store', dest='command', required=True)

args = parser.parse_args()

df = pd.read_csv(sys.stdin, index_col=0,header=0,decimal=dic[args.decimal])
df.replace('NA', np.nan, inplace=True)
df.replace('NaN', np.nan, inplace=True)
df.replace('Na', np.nan, inplace=True)
df = df.astype(float)
df.query(args.command,inplace=True)

output = StringIO()
df.to_csv(output)

print (output.getvalue())