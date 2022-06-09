#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.preprocessing import FunctionTransformer
import pandas as pd
import numpy as np
from io import StringIO
import argparse
import Util
from Base import Operator

class Log_Operator(Operator):

    def __init__(self) -> None:
        super().__init__()
        self.log_transformer = FunctionTransformer(self.log_transform)  

    def log_transform(self,x):
        return np.log(x + 1)
    
    def build_argparser(self):
        self._parser = argparse.ArgumentParser(description='Log transform ')
        self._parser=Util.add_argument_common(self._parser)
    
    def data_in(self):
        self.data=Util.input(self._parser)
    
    def procress(self):
        self.log_data=self.log_transformer.fit_transform(self.data)
        self.log_data.fillna(0)
        self.log_data = self.log_data[ np.isfinite( self.log_data ).all( axis = 1) ]
   
    def data_out(self):
        Util.output(self._parser,self.log_data)

if __name__ == '__main__':

    Log_Operator().run()