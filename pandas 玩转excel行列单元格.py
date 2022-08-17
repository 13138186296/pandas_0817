import pandas as pd
import numpy as np

# d = {'x':100,'y':300,'z':260}
# s1 = pd.Series(d)


# L1 = [100,200,300]
# L2 = ['x','y','z']
# s1 = pd.Series(L1,index=L2)
# s2 = pd.DataFrame(s1)

s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([4,5,6],index=[1,2,3],name='B')
s3 = pd.Series([7,8,9],index=[1,2,3],name='C')
s4 = pd.Series([10,11,12],index=[1,2,3],name='D')
df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})

df2 = pd.DataFrame([s1,s2,s3])
df3 = pd.DataFrame([s4])
print(df2)
print(df3)
df4 =pd.concat([df2,df3])
print(df4)