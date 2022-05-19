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
args = parser.parse_args()
output = StringIO()
df = pd.read_csv(sys.stdin, index_col=None,header=0,delimiter=dic[args.delimiter])
df.to_csv(output,header=True, index=True)
print (output.getvalue(), file = sys.stdout)
