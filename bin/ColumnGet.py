#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
import argparse
import pandas as pd
import sys

parser = argparse.ArgumentParser(description='Column Picker ')

dic={'csv':',','tsv':'\t','txt':' '}

parser.add_argument('-d','--delimiter', action='store', dest='delimiter',help='set input datasheet type:[csv|tsv|txt] ',default="csv")
parser.add_argument('-w','--wanted', action='store', dest='wanted',
                    default="")

args = parser.parse_args()

df = pd.read_csv(sys.stdin, index_col=0,header=0,delimiter=dic[args.delimiter])

df_list=[]
for c in args.wanted.split(" "):
    df_c=df[[c]]
    df_list.append(df_c)

df_out=pd.concat(df_list, axis=1, sort=False)

output = StringIO()
df_out.to_csv(output)

print (output.getvalue(), file = sys.stdout)