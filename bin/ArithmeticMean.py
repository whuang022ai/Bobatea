#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse


data=str(sys.stdin.read()).split(",")
data = list(filter(None, data))
print (np.mean(np.array(data).astype('float32') ), file = sys.stdout)