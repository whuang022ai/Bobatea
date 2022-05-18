#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
import argparse
import pandas as pd
import sys

parser = argparse.ArgumentParser(description='Column Drop ')

dic={'csv':',','tsv':'\t','txt':' '}

parser.add_argument('--d', action='store', dest='decimal',
                    default="csv")

parser.add_argument('--w', action='store', dest='wanted',
                    default="")

args = parser.parse_args()

df = pd.read_csv(sys.stdin, index_col=0,header=0,decimal=dic[args.decimal])

for c in args.wanted.split(" "):
    del df[c]


output = StringIO()
df.to_csv(output)

print (output.getvalue())