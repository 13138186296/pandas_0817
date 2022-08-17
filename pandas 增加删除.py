import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['A', 'B', 'C'])

# 输出DataFrame
print(df)
# 行列转至
print(df.T)

print(type(df['A']))
