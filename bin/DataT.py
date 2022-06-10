#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import StringIO
import argparse
import pandas as pd
from Base import Operator
import Util


class DataT_Operator(Operator):
    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(
            description='Data Transpose')
        self._parser = Util.add_argument_common(self._parser)
        self._parser = Util.remove_argument(
            self._parser, "input_matrix_transform")

    def data_in(self):
        delimiter_input = ','
        input_header = 0
        if self._args.file_type:
            delimiter_input = Util.file_delimiter[self._args.file_type]
        if self._args.delimiter:
            delimiter_input = self._args.delimiter
        # setting input headr
        if self._args.input_no_header:
            input_header = None
        else:
            input_header = self._args.header

        self.data = pd.read_csv(self._args.input, index_col=self._args.index_col,
                           header=input_header, delimiter=delimiter_input)

    def procress(self):
        self.data = pd.DataFrame(
            self.data.values.T, index=self.data.columns, columns=self.data.index)

    def data_out(self):
        Util.output(self._parser, self.data)


if __name__ == '__main__':

    DataT_Operator().run()
