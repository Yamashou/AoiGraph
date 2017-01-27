from graphviz import Digraph
import pandas as pd

def to_dictionary(df,serc,s_col,col):
    k = df[df['s_col'] == serc]
    dataList = [ i for i in k[col]]
    return {serc:dataList}
