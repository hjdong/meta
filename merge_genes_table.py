#!/usr/bin/env python3

import glob
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="用于合并多个基因表达文件")
parser.add_argument("--input",dest="inputFile",metavar="",help="需要合并文件的关键词")
parser.add_argument("--output",dest="outFile",metavar="",help="输出文件名")
args = parser.parse_args()

file_list = glob.glob('*'+args.inputFile+'*')

dfs = []
for filename in file_list:
	newName = filename.split('-')[0]
	df = pd.read_table(filename,index_col=[0])
	df.columns=[newName+'_max length',newName+'_read count',newName+'_rpkm',newName+'_IDs']
	dfs.append(df)

merge_dfs = dfs[0].join(dfs[1:])
merge_dfs.index.name='geneID'
merge_dfs.to_csv(args.outFile,sep="\t")
