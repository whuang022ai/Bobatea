#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from io import StringIO
import argparse
import pandas as pd
from Base import Operator

import Util


class CSVMerge_Operator(Operator):

    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):

        self._parser = argparse.ArgumentParser(description='CSV file merge ')
        self._parser.add_argument('-d1', '--file_type1', action='store', dest='file_type_1',
                                  help='set input left datasheet type:[csv|tsv|txt] ', default="csv")
        self._parser.add_argument('-1', '--left_datasheet', action='store',
                                  dest='left_datasheet_path', help='set input left datasheet')
        self._parser.add_argument('-ix1', '--index_col_left', action='store', dest='index_col_left', type=int,
                                  help='set input left datasheet index col (defult : None , with no col be set as index) ', default=None)
        self._parser.add_argument('-d2', '--file_type2', action='store', dest='file_type_2',
                                  help='set input right datasheet type:[csv|tsv|txt] ', default="csv")
        self._parser.add_argument('-2', '--right_datasheet', action='store',
                                  dest='right_datasheet_path', help='set input right datasheet')
        self._parser.add_argument('-ix2', '--index_col_right', action='store', dest='index_col_right', type=int,
                                  help='set input right datasheet index col (defult : None , with no col be set as index) ', default=None)
        self._parser = Util.add_argument_common_output(self._parser)

    def data_in(self):
       
        self.df_left = pd.read_csv(self._args.left_datasheet_path, index_col=self._args.index_col_left,
                                   header=0, delimiter=Util.file_delimiter[self._args.file_type_1])
        self.df_right = pd.read_csv(self._args.right_datasheet_path, index_col=self._args.index_col_right,
                                    header=0, delimiter=Util.file_delimiter[self._args.file_type_2])

    def procress(self):

        self.merge_df = self.df_left.merge(
            self.df_right, left_index=True, right_index=True)

    def data_out(self):
        Util.output(self._parser, self.merge_df)


if __name__ == '__main__':

    CSVMerge_Operator().run()
