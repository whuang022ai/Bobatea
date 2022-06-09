#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse
from sklearn import manifold
import Util
from Base import Operator


class tSNE_Operator(Operator):

    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(description='sklearn tSNE ')
        self._parser = Util.add_argument_common(self._parser)
        self._parser.add_argument('-n', '--n_components', action='store', dest='n_components',
                                  default=2, help='set tSNE output component number')
        self._parser.add_argument('-tsne', '--tsne_prefix', action='store', dest='tsne_prefix', default='tSNE',
                                  help='set the prefix name of each tSNE components (defult is \'tSNE\' , result will be tSNE1 , tSNE2 ... etc. )')

    def data_in(self):
        self.data = Util.input(self._parser)

    def procress(self):
        self.tSNE = manifold.TSNE(n_components=int(self._args.n_components))
        X_tSNE = self.tSNE.fit_transform(self.data)
        new_column = [str(self._args.tsne_prefix) + str(i + 1)
                      for i in range(X_tSNE.shape[1])]
        self.result = pd.DataFrame(
            X_tSNE, index=self.data.index, columns=new_column)

    def data_out(self):
        Util.output(self._parser, self.result)


if __name__ == '__main__':

    tSNE_Operator().run()
