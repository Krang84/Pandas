import pandas as pd
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9,3.2]
      }
#print(data)
frame = pd.DataFrame(data)
#print(frame)

frame2=pd.DataFrame(data, columns=["year", "state", "pop", "debt"], index=["one","two","three","four","five","six"])
frame2["year"]
frame2.loc["three"]

frame2 = pd.Series([1,2], index=["five","six"])

val= pd.Series([-1.2,-1.5,-1.7], index=["two","four","five"])

frame2["debt"]=val
