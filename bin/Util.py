#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import pandas
from io import StringIO
import matplotlib
from functools import wraps
from sys import exit, stderr, stdout
from traceback import print_exc
from errno import EPIPE

file_delimiter = {'csv': ',', 'tsv': '\t', 'txt': ' '}

class bcolors:
    # from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def suppress_broken_pipe_msg(f):
    # from https://stackoverflow.com/questions/14207708/ioerror-errno-32-broken-pipe-when-piping-prog-py-othercmd
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except SystemExit:
            raise
        except:
            print_exc()
            exit(1)
        finally:
            try:
                stdout.flush()
            finally:
                try:
                    stdout.close()
                finally:
                    try:
                        stderr.flush()
                    finally:
                        stderr.close()
    return wrapper


def add_argument_common(parser: argparse.ArgumentParser):

    parser.add_argument('-o', '--output', action='store', dest='output',
                        help='output result to file path (defult to standard output )', default=sys.stdout)
    parser.add_argument('-i', '--input', action='store', dest='input',
                        help='input to friom file path (defult to standard input )', default=sys.stdin)
    parser.add_argument('-ts', '--transform', action='store_true',
                        dest='input_matrix_transform',
                        help='input matrix transform (input.T)')
    parser.add_argument('-f', '--file_type', action='store',
                        dest='file_type', help='set input datasheet type:[csv|tsv|txt]', default='csv')
    parser.add_argument('-d', '--delimiter', action='store',
                        dest='delimiter', help='set input datasheet delimiter ')
    parser.add_argument('-ix', '--index_col', action='store', dest='index_col', type=int,
                        help='set input datasheet index col (defult : None , with no col be set as index) ', default=None)
    parser.add_argument('-header', '--header', action='store', dest='header', type=int,
                        help='set input datasheet header (defult : 0) : the first line (row = 0) of file will be the header', default=0)
    parser.add_argument('-inh', '--input_no_header', action='store_true',
                        dest='input_no_header', help='set input datasheet with no header when read in')
    parser.add_argument('-ox', '--output_with_index', action='store_true',
                        dest='output_with_index', help='set output datasheet with index', default=False)

    return parser


def add_argument_plot(parser: argparse.ArgumentParser):

    parser.add_argument('-t', '--title', action='store', dest='title', help='set plot title',
                        default="plot")
    parser.add_argument('-xl', '--xlabel', action='store', dest='xlabel', help='set x-axis label',
                        default="x")
    parser.add_argument('-yl', '--ylabel', action='store', dest='ylabel', help='set y-axis label',
                        default="y")
    parser.add_argument('-img', '--output_img', action='store',
                        dest='output_img', help='output image to file path ')

    return parser


def input(parser: argparse.ArgumentParser):
    args = parser.parse_args()
    # setting delimiter
    delimiter_input = ','
    input_header = 0
    if args.file_type:
        delimiter_input = file_delimiter[args.file_type]
    if args.delimiter:
        delimiter_input = args.delimiter
    # setting input headr
    if args.input_no_header:
        input_header = None
    else:
        input_header = args.header

    data = pandas.read_csv(args.input, index_col=args.index_col,
                           header=input_header, delimiter=delimiter_input)

    if args.input_matrix_transform:
        X = data.values.T
        index = data.columns
        header = data.index
    else:
        X = data.values
        index = data.index
        header = data.columns
    data = pandas.DataFrame(X, index=index, columns=header)
    return data



def output(parser: argparse.ArgumentParser, data: pandas.DataFrame):
    args = parser.parse_args()
    output_to_file(file=args.output,data=data,index=args.index_col,header=True)


@suppress_broken_pipe_msg
def output_to_file(file, data: pandas.DataFrame ,index : int ,header=True):
    try:
        broken_pipe_exception = BrokenPipeError
    except NameError:  # Python 2
        broken_pipe_exception = IOError
    try:
        output_buff = StringIO()
        data.to_csv(output_buff, header=header, index=index)
        print(output_buff.getvalue(), file=file)
        #print(output_buff.getvalue(), file=output_buff)
    except broken_pipe_exception as exc:
        if broken_pipe_exception == IOError:
            if exc.errno != EPIPE:
                raise


def savefig_autoformat(output_img_path: str, fig):
    if output_img_path.endswith((".png", ".svg", ".pdf")):
        fig.savefig(output_img_path, format=output_img_path.split(".")[-1])
    else:
        fig.savefig(output_img_path+'.png', format='png')
