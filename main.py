from graphviz import Digraph
import pandas as pd
from typing import Dict, Tuple, List

class GetPlot:
    def __init__(self, df:pd.DataFrame, G:Digraph):
        self.df = df
        self.G = G

    def list_to_zip(self,list: List[str]):
        return zip(v1, v2)

    def get_days(self,year=2016,month=10,day=1,days=1):#-> None
        start = str(year)+"/"+str(month)+"/"
        serch_days = []
        for serch_day in range(day,days+day):
            serch_days.append(start+'%s' % '{0:02d}'.format(serch_day))
        self.days = serch_days

    def get_df_serch_days(self,col_days_name:str):#-> None
        self.df_serch_days_list = []
        ten = '.....'
        for day in self.days:
            self.df_serch_days_list.append(self.df[self.df[col_days_name].str.contains(day + ten)])

    def to_dictionary(self, serc: int, s_col: str, col: str):#->Dict[str,List[str]]
        k = df[df[s_col] == serc]
        data_list = [i for i in k[col]]
        name = str(serc)
        return {name: data_list}

    def drop_duplicates_main(self,col_name:str):
        self.df_drop = self.df.drop_duplicates([col_name])

    def drop_duplicates_days_list(self,col_name:str):
        self.df_serch_days_list_drop = [k.drop_duplicates([col_name]) for k in self.df_serch_days_list]




if __name__ == '__main__':
    df = pd.read_csv("/Volumes/Transcend/archive/TranData_headerNUM.csv")
    u = Digraph('unix', filename='unix.gv')
    u.body.append('size="8,8"')
    u.node_attr.update(color='lightblue2', style='filled')
    c = GetPlot(df,u)
    data = c.to_dictionary( 4432, '会社コード_2', 'お買い上げ金額_8')
    c.get_days()
    c.get_df_serch_days("日付_1")
    print(len(c.df_serch_days_list))
    print(c.days)
    print(data['4432'][1])
