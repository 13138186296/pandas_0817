import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./data/tongji.xlsx')
result = df.head(100)
result.sort_values(by='总邮资',inplace=True,ascending=False)

print(result)
# result.plot.bar(x='寄件人',y='总邮资',title='test')
plt.bar(result['寄件人'],result['总邮资'],color='blue')
plt.xlabel('寄件人')
plt.ylabel('邮费')
plt.title('分析表',fontsize=14)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.tight_layout()
plt.show()