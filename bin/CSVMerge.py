#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from io import StringIO
import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='csv merge ')

dic={'csv':',','tsv':'\t','txt':' '}



parser.add_argument('-d1','--delimiter1', action='store', dest='delimiter_1',help='set input left datasheet type:[csv|tsv|txt] ',default="csv")
parser.add_argument('-1','--left_datasheet', action='store', dest='left_datasheet_path',help='set input left datasheet')


parser.add_argument('-d2','--delimiter2', action='store', dest='delimiter_2',help='set input right datasheet type:[csv|tsv|txt] ',default="csv")
parser.add_argument('-2','--right_datasheet', action='store', dest='right_datasheet_path',help='set input right datasheet')
args = parser.parse_args()

df = pd.read_csv(args.left_datasheet_path, index_col=None,header=0,delimiter=dic[args.delimiter_1])
df2 = pd.read_csv(args.right_datasheet_path, index_col=None,header=0,delimiter=dic[args.delimiter_2])

merge_df = df.merge(df2, left_index=True, right_index=True)

output = StringIO()
merge_df.to_csv(output,index=False)

print (output.getvalue(), file = sys.stdout)