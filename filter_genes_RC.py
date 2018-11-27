#!/usr/bin/env python3

import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="用于过滤样品中RC均小于10的基因")
parser.add_argument("-i",dest="inputFile",metavar="",help="输入文件名")
parser.add_argument("-o",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

df = pd.read_table(args.inputFile,index_col=[0])
dff = df[(df.iloc[:,1:]>=10).any(1)]

dff.to_csv(args.outFile,sep="\t")
