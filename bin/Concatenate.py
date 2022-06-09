#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import argparse
import Util
import sys
from io import StringIO

if ("-" in ''.join(sys.argv)):
    # build parser
    parser = argparse.ArgumentParser(description='concatenate or print datasheet')
    parser=Util.add_argument_common(parser)
    # read input
    data=Util.input(parser)
    # print output
    Util.output(parser,data)
else:
    # using only postions
    if len(sys.argv) ==1: # read file from sys.stdin
        data=pd.read_csv(sys.stdin, index_col=None,header=0)
        Util.output_to_file(sys.stdout,data,None,True)
    elif len(sys.argv) ==2: # read file from sys.argv[1]
        data=pd.read_csv(sys.argv[1], index_col=None,header=0)
        Util.output_to_file(sys.stdout,data,None,True)
    # not supported kat a b yet. 

