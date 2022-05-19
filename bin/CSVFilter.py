#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import numpy as np
from io import StringIO
import argparse

parser = argparse.ArgumentParser(description='csv/tsv/txt dataframe filter ')
dic={'csv':',','tsv':'\t','txt':' '}
parser.add_argument('-d','--delimiter', action='store', dest='delimiter',help='set input datasheet type:[csv|tsv|txt] ',default="csv")
parser.add_argument('-c','--cmd', action='store', dest='command',help='set filter condiction', required=True)
args = parser.parse_args()
df = pd.read_csv(sys.stdin, index_col=0,header=0,delimiter=dic[args.delimiter])
df.replace('NA', np.nan, inplace=True)
df.replace('NaN', np.nan, inplace=True)
df.replace('Na', np.nan, inplace=True)
df = df.astype(float)
df.query(args.command,inplace=True)
output = StringIO()
df.to_csv(output)
print (output.getvalue(), file = sys.stdout)
