#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np
from io import StringIO
import argparse
from scipy.interpolate import interp1d
from dateutil.parser import parse
import Util
from Base import Operator


class Curve_Plot_Operator(Operator):

    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        super().__init__()

    def is_date(self, string, fuzzy=False):
        """
        Return whether the string can be interpreted as a date.

        :param string: str, string to check for date
        :param fuzzy: bool, ignore unknown tokens in string if True
        ref: https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
        """
        string = str(string)
        try:
            parse(string, fuzzy=fuzzy)
            return True

        except ValueError:
            return False

    def build_argparser(self):

        self._parser = argparse.ArgumentParser(
            description='Matplotlib smooth line curve plot ')
        self._parser = Util.add_argument_common(self._parser)
        self._parser = Util.add_argument_plot(self._parser)
        self._parser.add_argument('-x', '--xname', action='store', dest='xname', help='get x-axis data',
                                  default="x")
        self._parser.add_argument('-y', '--yname', action='store', dest='yname', help='get y-axis data',
                                  default="y")
        self._parser.add_argument('-xtn', '--x_tick_number', action='store', dest='x_tick_number', help='set x ticks number',
                                  default=None)
        self._parser.add_argument(
            '-s', '--smooth', action='store_true', dest='smooth', help='set smooth curve')
        self._parser.add_argument(
            '-p', '--datapoint', action='store_true', dest='datapoint', help='set data point')

    def data_in(self):

        self.data = Util.input(self._parser)
        self.data = self.data[[self._args.xname, self._args.yname]]

    def procress(self):

        if self._args.smooth:

            if type(self.data.values[0, 0]) is str:
                if self.is_date(self.data.values[0, 0]):
                    x = list(range(len(self.data.values[:, 1])))
                    spline_model = interp1d(
                        x, self.data.values[:, 1], kind='cubic')
                    self.pseudo_x = np.linspace(min(x), max(x), 500)
                    self.pseudo_y = spline_model(self.pseudo_x)
                    self.ax.plot(self.pseudo_x, self.pseudo_y, '-')
                else:
                    raise ValueError('x-axis can not be string')
            else:
                spline_model = interp1d(
                    self.data.values[:, 0], self.data.values[:, 1], kind='cubic')
                self.pseudo_x = np.linspace(
                    self.data.values[:, 0].min(), self.data.values[:, 0].max(), 500)
                self.pseudo_y = spline_model(self.pseudo_x)
                self.ax.plot(self.pseudo_x, self.pseudo_y, '-')

        else:
            self.ax.plot(self.data.values[:, 0], self.data.values[:, 1], '-')
        if self._args.datapoint:
            self.ax.plot(self.data.values[:, 0], self.data.values[:, 1], 'o')
        self.ax.set_title(self._args.title)
        self.ax.set_xlabel(self._args.xlabel)
        self.ax.set_ylabel(self._args.ylabel)

        plt.xticks(rotation=90)

        if self._args.x_tick_number is None:
            self._args.x_tick_number = len(self.data.values[:, 0])

        self.ax.xaxis.set_major_locator(
            plt.MaxNLocator(self._args.x_tick_number))

        plt.show()

    def data_out(self):
        Util.output(self._parser, self.data)


if __name__ == '__main__':

    Curve_Plot_Operator().run()
