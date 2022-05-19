#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import numpy as np
from io import StringIO
import argparse

parser = argparse.ArgumentParser(description='add header')
parser.add_argument('--h', action='store', dest='header')
args = parser.parse_args()
output = StringIO()
output.write(args.header)
output.write("\n")
for input in sys.stdin.readlines():
    output.write(input)
print (output.getvalue(),end="", file = sys.stdout)
