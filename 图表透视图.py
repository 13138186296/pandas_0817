import pandas as pd

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_rows',None)

# df = pd.read_excel('./data/tongji.xlsx')
# result = df.head(100)
# result.sort_values(by='总邮资',inplace=True,ascending=False)
#
# print(result)
# # result.plot.bar(x='寄件人',y='总邮资',title='test')
# plt.bar(result['寄件人'],result['总邮资'],color='blue')
# plt.xlabel('寄件人')
# plt.ylabel('邮费')
# plt.title('分析表',fontsize=14)
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.tight_layout()
# plt.show()


# 数据透视
df = pd.read_excel('./data/6.xls')
# dfa = df.pivot_table(index='寄件人',columns='日期',values='总邮资')
print(df)
