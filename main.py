from graphviz import Digraph
import pandas as pd


def to_dictionary(df, serc, s_col, col):
    k = df[df[s_col] == serc]
    dataList = [i for i in k[col]]
    name = str(serc)
    return {name: dataList}

if __name__ == '__main__':
    df = pd.read_csv("../../TranData_headerNUM.csv")
    data = to_dictionary(df, 4432, '会社コード_2', 'お買い上げ金額_8')
    print(data['4432'][0])
