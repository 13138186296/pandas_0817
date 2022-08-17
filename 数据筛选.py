import pandas as pd


def age_18_to_30(a):
    return 5<=a<10

def level_a(a):
    return 20<=a<30
df = pd.read_excel('./data/6.xls')

# 第一种方法
# df = df.loc[df['总邮资'].apply(age_18_to_30)]
# print(df)
#

# 第二种方法

# df = df.loc[df['总邮资'].apply(lambda a: 1<=a<5)].loc[df['日期'].apply(lambda a: 1<=a<=30)]
# print(df)


# 计算不同省份的快递费

result = df.loc[df['寄达省名称'] == '浙江省']
print(result[['可售卖产品', '邮件号', '寄件人', '寄达省名称', '重量(克)', '总邮资']])

# res = df.groupby('寄件人').sum()
# print(res)
#
# # resa = pd.DataFrame([res])
#
# res.to_excel('./data/tongji.xlsx')
