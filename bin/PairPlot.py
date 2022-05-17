#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import pandas as pd
from io import StringIO
import argparse
import seaborn as sns


parser = argparse.ArgumentParser(description='Seaborn pairplot')
args = parser.parse_args()



data = pd.read_csv(sys.stdin, index_col=0,header=0)
output = StringIO()
data.to_csv(output)

print (output.getvalue())
sns.pairplot(data)

plt.show()