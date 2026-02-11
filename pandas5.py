import pandas as pd
series=pd.Series([1,2,3,4,5], index=['a','b','c','d','c'])
series[2:]
#c    3
#d    4
#c    5
#dtype: int64
