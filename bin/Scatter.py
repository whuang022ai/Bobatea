#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse


parser = argparse.ArgumentParser(description='Matplotlib scatter plot ')

parser.add_argument('--t', action='store', dest='title',
                    default="scatter plot")

parser.add_argument('--x', action='store', dest='xlabel',
                    default="x")
parser.add_argument('--y', action='store', dest='ylabel',
                    default="y")

args = parser.parse_args()

fig, ax = plt.subplots()


data = pd.read_csv(sys.stdin, index_col=0,header=0)
output = StringIO()
data.to_csv(output)

print (output.getvalue())

ax.plot(data.values[:, 0], data.values[:, 1], 'o')
ax.set_title(args.title)
ax.set_xlabel(args.xlabel)
ax.set_ylabel(args.ylabel)
for i, marker in enumerate(data.index):
    ax.annotate(marker, (data.values[i, 0], data.values[i, 1] ), fontsize=6)



plt.show()