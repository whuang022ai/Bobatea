#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse
import Util
# build parser
parser = argparse.ArgumentParser(description='Matplotlib scatter plot ')
parser=Util.add_argument_common(parser)
parser=Util.add_argument_plot(parser)
args = parser.parse_args()
# set ax
fig, ax = plt.subplots()
# read input
data=Util.input(parser)
Util.output(parser,data)
# plot data
ax.plot(data.values[:, 0], data.values[:, 1], 'o')
ax.set_title(args.title)
ax.set_xlabel(args.xlabel)
ax.set_ylabel(args.ylabel)
# anno scatter plot
for i, marker in enumerate(data.index):
    ax.annotate(marker, (data.values[i, 0], data.values[i, 1] ), fontsize=6)
# output fig
if args.output_img:
    Util.savefig_autoformat(args.output_img,fig)
else:
    plt.show()
