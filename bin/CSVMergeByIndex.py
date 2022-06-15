#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys
import Util

files = sys.argv[1:]

result = pd.DataFrame()

for file in files:
    df = pd.read_csv(file, index_col=0)
    result = result.join(df, how='outer')

Util.output_to_file(sys.stdout, result, True, header=True)
