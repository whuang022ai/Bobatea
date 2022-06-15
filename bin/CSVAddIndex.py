#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import numpy as np
from io import StringIO
import argparse
from Base import Operator
import Util


class CSVAddIndex_Operator(Operator):
    def __init__(self) -> None:
        super().__init__()

    def build_argparser(self):
        self._parser = argparse.ArgumentParser(description='Add index for CSV')
        self._parser = Util.add_argument_common(self._parser)

    def data_in(self):

        self.data = Util.input(self._parser)

    def procress(self):
        pass

    def data_out(self):
        output = StringIO()
        self.data.to_csv(output, header=True, index=True)
        print(output.getvalue(), file=sys.stdout)


if __name__ == '__main__':

    CSVAddIndex_Operator().run()
