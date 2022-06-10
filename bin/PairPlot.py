#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import pandas as pd
from io import StringIO
import argparse
import seaborn as sns
import Util
from Base import Operator


class PairPlot_Operator(Operator):

    def __init__(self) -> None:

        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(description='Seaborn pairplot')
        self._parser.add_argument('-t', '--title', action='store', dest='title', help='set plot title',
                                  default="")
        self._parser=Util.add_argument_common(self._parser)

    def data_in(self):
        self.data = Util.input(self._parser)

    def procress(self):
        self.ax = sns.pairplot(self.data)
        self.ax.fig.suptitle(self._args.title)

    def data_out(self):
        Util.output(self._parser, self.data)
        plt.show()


if __name__ == '__main__':

    PairPlot_Operator().run()
