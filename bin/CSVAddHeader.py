#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import numpy as np
from io import StringIO
import argparse

parser = argparse.ArgumentParser(description='add header')

dic={'csv':',','tsv':'\t','txt':' '}

parser.add_argument('--d', action='store', dest='decimal',
                    default="csv")
parser.add_argument('--h', action='store', dest='header')
parser.add_argument('--x', action='store_true',
                    dest='input_with_no_index')
args = parser.parse_args()

output = StringIO()

header=args.header.split(" ")
ix=0
if args.input_with_no_index:
    ix=None
df = pd.read_csv(sys.stdin, index_col=ix,header=None,decimal=dic[args.decimal])
df.columns =header
df.to_csv(output,header=True, index=None)

print (output.getvalue())