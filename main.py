from graphviz import Digraph
import pandas as pd

class getPlot:
    def __init__(self, df, G):
        self.df = df
        self.G = G

    def to_dictionary(self, serc, s_col, col):
        k = self.df[self.df[s_col] == serc]
        dataList = [i for i in k[col]]
        name = str(serc)
        return {name: dataList}

if __name__ == '__main__':
    df = pd.read_csv("../../TranData_headerNUM.csv")
    u = Digraph('unix', filename='unix.gv')
    u.body.append('size="8,8"')
    u.node_attr.update(color='lightblue2', style='filled')
    c = getPlot(df,u)
    data = c.to_dictionary( 4432, '会社コード_2', 'お買い上げ金額_8')
    print(data['4432'][0])
