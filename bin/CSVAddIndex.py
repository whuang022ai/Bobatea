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
args = parser.parse_args()

output = StringIO()


df = pd.read_csv(sys.stdin, index_col=None,header=0,decimal=dic[args.decimal])

df.to_csv(output,header=True, index=True)

print (output.getvalue())