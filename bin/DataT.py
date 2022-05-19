#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import StringIO
import argparse
import pandas as pd

data = pd.read_csv(sys.stdin, index_col=0)
output = StringIO()
pd.DataFrame( data.values.T, index= data.columns, columns=data.index).to_csv(output,header=True, index=True)
print (output.getvalue(), file = sys.stdout)
