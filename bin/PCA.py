#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import argparse
import Util
from Base import Operator


class PCA_Operator(Operator):

    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(description='sklearn PCA ')
        self._parser = Util.add_argument_common(self._parser)
        self._parser.add_argument('-n', '--n_components', action='store', dest='n_components',
                                  default=2, help='set pca output component number')
        self._parser.add_argument('-e', '--expr', action='store',
                                  dest='explained_variance_ratio_outputpath', help='set output path of explained variance ratio for each components')
        self._parser.add_argument('-pc', '--pc_prefix', action='store', dest='pc_prefix', default='PC',
                                  help='set the prefix name of each principal components (defult is \'PC\' , result will be PC1 , PC2 ... etc. )')

    def data_in(self):
        self.data = Util.input(self._parser)

    def procress(self):
        self.pca = PCA(n_components=int(self._args.n_components))
        X_pca = self.pca.fit_transform(self.data.values)
        new_column = [str(self._args.pc_prefix) + str(i + 1)
                      for i in range(X_pca.shape[1])]
        self.result = pd.DataFrame(
            X_pca, index=self.data.index, columns=new_column)

    def data_out(self):
        Util.output(self._parser, self.result)
        if self._args.explained_variance_ratio_outputpath:
            np.savetxt(self._args.explained_variance_ratio_outputpath,
                       self.pca.explained_variance_ratio_ * 100, delimiter=',',
                       fmt='%f')


if __name__ == '__main__':

    PCA_Operator().run()
