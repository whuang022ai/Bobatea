#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import argparse
import Util
from Base import Operator

class ScatterPlot_Operator(Operator):

    def __init__(self) -> None:

        self.fig,  self.ax = plt.subplots()
        super().__init__()
    
    def build_argparser(self):

        self._parser = argparse.ArgumentParser(description='Matplotlib scatter plot ')
        self._parser=Util.add_argument_common(self._parser)
        self._parser=Util.add_argument_plot(self._parser)
    
    def data_in(self):
        self.data=Util.input(self._parser)
    
    def procress(self):
        self.ax.plot(self.data.values[:, 0], self.data.values[:, 1], 'o')
        self.ax.set_title(self._args.title)
        self.ax.set_xlabel(self._args.xlabel)
        self.ax.set_ylabel(self._args.ylabel)
        # anno
        for i, marker in enumerate(self.data.index):
            self.ax.annotate(marker, (self.data.values[i, 0], self.data.values[i, 1] ), fontsize=6)
    
    def data_out(self):
        Util.output(self._parser,self.data)
        if self._args.output_img:
            Util.savefig_autoformat(self._args.output_img,self.fig)
        else:
            plt.show()

if __name__ == '__main__':

    ScatterPlot_Operator().run()