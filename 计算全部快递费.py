import pandas as pd
import openpyxl

zb = pd.read_excel('./data/6.xls')

print(zb)
price = zb.groupby('寄件人').sum()
print(price)

num = zb.groupby('寄件人')[['总邮资','日期']].count()
print('列的名称：',num)
num.columns = ['总单数','服务费*0.4']
danshu = num['总单数']
print(danshu)

fuwufei = num['服务费*0.4'] *0.4
print(fuwufei)

zongjiage = price['总邮资']+fuwufei

print(zongjiage)
total = pd.concat([price,danshu,fuwufei,zongjiage],axis=1)
total.columns = ['邮件号', '重量(克)', '总邮资', '日期', '总单数', '服务费*0.4', '总费用']
total.to_excel('./data/6月份快递费统计.xlsx')
