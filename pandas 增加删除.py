import pandas as pd

data = [10, 11, 12]
index = ['a', 'b', 'c']

s = pd.Series(data=data, index=index)
print(s[0])
print(s[0:2])

print(s.loc['a'])

s1 = s.copy()
s1['a'] = 100

s1.replace(to_replace=100, value=101, inplace=True)
print(s1)

# 更改索引

s1.rename(index={'a': 'A'}, inplace=True)

print(s1)
