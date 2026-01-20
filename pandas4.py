import pandas as pd
series1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','c'])
a    1
b    2
c    3
d    4
c    5
dtype: int64
series1.loc['c']
c    3
c    5
dtype: int64
