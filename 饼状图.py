import  pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./data/tongji.xlsx',index_col='寄件人')
print(df)

df['总邮资'].plot.pie(fontsize=8,counterclock=False,startangle=-270)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('快递费占比',fontsize=16,fontweight='bold')
plt.show()