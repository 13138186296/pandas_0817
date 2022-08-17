import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_excel('./data/6.xls')
result = df.loc[df['寄达省名称'] == '广东省']
print(result)
