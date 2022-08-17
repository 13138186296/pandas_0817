import pandas as pd
import openpyxl

df = pd.read_excel('./data/6.xls')

# 设置列的名称
df.columns = ['product','code','name','provice','weight','price','date']

# 设置索引
# df.set_index('id',inplace=True)

# print(df)
# print(df.shape)
# print(df.columns)
print(df.columns)
result = df[df['name']=='平']
# df.to_excel('./data/news_6.xlsx')
