#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import numpy as np
from io import StringIO
import argparse
import Util
from Base import Operator


class CSVAddHeader_Operator(Operator):

    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(description='Add header of CSV')
        self._parser.add_argument(
            '--h', action='store', dest='header')

    def data_in(self):
        pass

    def procress(self):
        pass

    def data_out(self):
        output = StringIO()
        output.write(self._args.header)
        output.write("\n")
        for input in sys.stdin.readlines():
            output.write(input)
        print(output.getvalue(), end="", file=sys.stdout)


if __name__ == '__main__':

    CSVAddHeader_Operator().run()
