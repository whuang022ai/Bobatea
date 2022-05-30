#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse
from scipy.interpolate import interp1d
from dateutil.parser import parse
import pickle

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    string=str(string)
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

parser = argparse.ArgumentParser(description='Matplotlib smooth line curve plot ')

parser.add_argument('-t','--title', action='store', dest='title', help='set plot title',
                    default="scatter plot")

parser.add_argument('-xl','--xlabel', action='store', dest='xlabel',help='set x-axis label',
                    default="x")
parser.add_argument('-yl','--ylabel', action='store', dest='ylabel',help='set y-axis label',
                    default="y")
parser.add_argument('-x','--xname', action='store', dest='xname',help='get x-axis data',
                    default="x")
parser.add_argument('-y','--yname', action='store', dest='yname',help='get y-axis data',
                    default="y")
parser.add_argument('-xtn','--x_tick_number', action='store', dest='x_tick_number',help='set x ticks number',
                    default=None)
parser.add_argument('-s','--smooth', action='store_true', dest='smooth',help='set smooth curve')
parser.add_argument('-p','--datapoint', action='store_true', dest='datapoint',help='set data point')


args = parser.parse_args()
smooth=args.smooth
fig, ax = plt.subplots()


data = pd.read_csv(sys.stdin, index_col=0,header=0)
data=data[[args.xname,args.yname]]

output = StringIO()
data.to_csv(output)

print (output.getvalue(), file = sys.stdout)

if smooth:

    if type(data.values[0, 0]) is  str:
        if is_date(data.values[0, 0]):
            x=list(range (len( data.values[:, 1])))
            spline_model = interp1d(x, data.values[:, 1], kind='cubic')
            pseudo_x = np.linspace(min(x),max(x), 500)
            pseudo_y = spline_model(pseudo_x)
            ax.plot(pseudo_x, pseudo_y, '-')
        else:
            raise ValueError('x-axis can not be string')
    else:
        spline_model =interp1d(data.values[:, 0], data.values[:, 1], kind='cubic')
        pseudo_x = np.linspace(data.values[:, 0].min(), data.values[:, 0].max(), 500)
        pseudo_y = spline_model(pseudo_x)
        ax.plot(pseudo_x, pseudo_y, '-')

else:
    ax.plot(data.values[:, 0], data.values[:, 1], '-')
if args.datapoint:
    ax.plot(data.values[:, 0], data.values[:, 1], 'o')
ax.set_title(args.title)
ax.set_xlabel(args.xlabel)
ax.set_ylabel(args.ylabel)
plt.xticks(rotation=90)
if args.x_tick_number is None:
    args.x_tick_number=len(data.values[:, 0])
ax.xaxis.set_major_locator(plt.MaxNLocator(args.x_tick_number))

with open('test.ax.1', 'wb') as f:
    pickle.dump(ax, f)
    
plt.show()