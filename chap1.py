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

# learn
# pd.DataFrame(dict)

# Example 1

data = {"state":["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year":[2000,2001,2002,2001,2002,2003],
        "pop":[1.5,1.7,3.6,2.4,2.9,3.2] }
frame = pd.DataFrame(data)

