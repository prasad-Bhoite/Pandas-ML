import pandas as pd

#Creating Series in Pandas
data = [1,2,3,4,5]
series = pd.Series(data,index=['A','B','C','D','E'])
print(series)



#Creating DataFrame in pandas...
data = { 'Name' : ['Prasad','Nikita','Pooja','Malhar','Rushi'],
         'Age' : [22,23,20,23,23],
         'Color' : ['White','Black','Red','Yellow','Blue']
       }

df = pd.DataFrame(data)
print(df)
