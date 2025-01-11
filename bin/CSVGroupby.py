#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
from Base import Operator
import argparse
import Util


class CSVGropupby_Operator(Operator):

    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(
            description='CSV groupby')
        self._parser = Util.add_argument_common(self._parser)
        self._parser.add_argument('-b', '--by', action='store',
                                  dest='by', help='set the column name to group')

    def data_in(self):
        self.data = Util.input(self._parser)

    def procress(self):
        self.groups = self.data.groupby(by=self._args.by)
        for name, group in self.groups:
            print(name)
            print(group)

    def data_out(self):
        pass


if __name__ == '__main__':

    CSVGropupby_Operator().run()
