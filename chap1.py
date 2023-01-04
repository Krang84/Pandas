# create a dataframe with a dict and DataFrame()

# How To !!!
import pandas as pd

# create a dict
my_dict = { "column1": [1,2,3], 
           "column2": [4,5,6] }
# use pd.DataFrame(dict)
frame = pd.DataFrame(my_dict)

# column1   column1
#    1         4
#    2         5
#    3         6

