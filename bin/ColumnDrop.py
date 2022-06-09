#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
import argparse
from warnings import catch_warnings
import pandas as pd
import sys
import Util
from Base import Operator
from os.path import exists


class ColumnDrop_Operator(Operator):
    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(description='Column Drop')
        self._parser = Util.add_argument_common(self._parser)
        self._parser.add_argument('-dr', '--drop', action='store', dest='drop',
                                      default="",help='the columns want to drop from datasheet , sperate by \',\'  ')
        if ("-" in ''.join(sys.argv)):
            self.flag = True
        else:
            self.flag = False
            if len(sys.argv)==1:
                self._parser.print_help(sys.stderr)
                print('another way to use without argument flags can done by :')
                print('ColumnDrop.py [file|column1] [column2] ...')
                sys.exit(1)

    def data_in(self):
        if self.flag:  # using the argparse with - and -- to procress
            self.data = Util.input(self._parser)
        else:  # without - or --
            # if the fisrt argv is a file to read in , for example : drop iris.csv petal_width species
            if exists(sys.argv[1]):
                self.data = pd.read_csv(sys.argv[1], index_col=None, header=0)
                self.start_f = 2
            else:  # the fisrt argv is a column to drop , for example : cat iris.csv |drop petal_width species
                self.data = pd.read_csv(sys.stdin, index_col=None, header=0)
                self.start_f = 1

    def df_drop(self, col_list, df):
        drop=False
        for col_to_drop in col_list:
            try:
                del self.data[col_to_drop]
                drop = True
            except KeyError as e:
                print(Util.bcolors.FAIL+'Error , column \''+col_to_drop +
                      "\' not in the datasheet , the column will be ignore.!"+Util.bcolors.ENDC, file=sys.stderr)
        if not drop:
            print(Util.bcolors.FAIL+'Error, any columns that want to drop had not existed in the datasheet.The result will be same as input'+Util.bcolors.ENDC)
        return self.data

    def procress(self):

        if self.flag:
            col_list = self._args.drop.split(",")
            self.result = self.df_drop(col_list, self.data)
        else:
            col_list = sys.argv[self.start_f:]
            self.result = self.df_drop(col_list, self.data)

    def data_out(self):
        if self.flag:
            Util.output(self._parser, self.result)
        else:
            Util.output_to_file(sys.stdout, self.result, None, True)

    def run(self):
        self.build_argparser()
        if self.flag:
            self._args = self._parser.parse_args()
        self.data_in()
        self.procress()
        self.data_out()


if __name__ == '__main__':

    ColumnDrop_Operator().run()
