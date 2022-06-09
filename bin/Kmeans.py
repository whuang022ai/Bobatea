#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import seaborn as sns
import Util
from Base import Operator


class Kmeans_Operator(Operator):

    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(
            description='sklearn Kmeans (with plot)')
        self._parser = Util.add_argument_common(self._parser)
        self._parser = Util.add_argument_plot(self._parser)
        self._parser.add_argument('-n', '--n_clusters', action='store', dest='n_clusters',
                                  default=3, help='set k-means output cluster number', type=int)
        self._parser.add_argument('-no_plot', '--no_plot', action='store_true',
                                  dest='no_plot', help='set flag will not plot the kmeans result')
        self._parser.add_argument('-in', '--init', action='store', dest='init', default='k-means++',
                                  help='set sklearn k-means init parameter [k-means++|random] , defult is k-means++')

    def data_in(self):
        self.data = Util.input(self._parser)

    def procress(self):
        model = KMeans(init=self._args.init,
                       n_clusters=self._args.n_clusters, n_init=self._args.n_clusters*3)
        model.fit(self.data)
        self.data['kmeans_predicted_cluster'] = model.labels_.astype(int)

    def data_out(self):
        Util.output(self._parser, self.data)
        if self._args.no_plot:
            quit()
        sns.scatterplot(x=self.data.columns[0], y=self.data.columns[1],
                        hue="kmeans_predicted_cluster", data=self.data, ax=self.ax)
        # anno scatter plot
        for i, marker in enumerate(self.data.index):
            self.ax.annotate(
                marker, (self.data.values[i, 0], self.data.values[i, 1]), fontsize=6)
        # output fig
        if self._args.output_img:
            Util.savefig_autoformat(self._args.output_img, self.fig)
        else:
            plt.show()


if __name__ == '__main__':

    Kmeans_Operator().run()
