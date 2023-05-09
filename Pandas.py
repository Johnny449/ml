#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
arr=np.array([10,15,18,22,55,77])
s=pd.Series(arr)
print(s)
print(s.loc[:2])
print(s.loc[3:4])
s.loc[2:3]


# In[9]:


arr=np.array(['a','b','c','d'])
s=pd.Series(arr,index=['first','scond','third','fourth'])
print(s)
print('\n')
print(s.index)


# In[11]:


s=pd.Series(['a','b','c','d'])
df=pd.DataFrame(s)
print(df)


# In[13]:


name=pd.Series(['Hardik','Virat'])
team=pd.Series(['MI','RCB'])
dic={'Name':name,'Team':team}
df=pd.DataFrame(dic)
print(df)


# In[14]:


l=[{'Name':'Sachin','SirName':'Bhardwaj'},
  {'Name':'Vinod','SirName':'Verma'}]
df1=pd.DataFrame(l)
print(df1)
for(row_index,row_value) in df1.iterrows():
    print('\n Row index is ::',row_index)
    print('Row value is ::')
    print(row_value)


# In[15]:


l=[{'Name':'Sachin','SirName':'Bhardwaj'},
  {'Name':'Vinod','SirName':'Verma'}]
df1=pd.DataFrame(l)
print(df1)
for(col_name,col_value) in df1.iterrows():
    print('\n Column name is ::',col_name)
    print('Column value is ::')
    print(col_value)


# In[21]:


s = pd.Series([10,15,18,22])
df=pd.DataFrame(s)
df.columns=['List1']
df['List2']=20
df['List3']=df['List1']+df['List2']
print(df)
del df['List3']
print(df)
df.pop('List2')
print(df)


# In[23]:


s= pd.Series([10,20,30,40])
df=pd.DataFrame(s)
df.columns=['List1']
df['List2']=40
df1=df.drop('List2',axis=1)
df2=df.drop(index=[2,3],axis=0)
print(df)
print("After deletion::")
print(df1)
print ("After row deletion::")
print(df2)


# In[24]:




empdata={ 'Doj':['12-01-2012','15-01-2012','05-09-2007',
'17-01-2012','05-09-2007','16-01-2012'],
'empid':[101,102,103,104,105,106],

'ename':['Sachin','Vinod','Lakhbir','Anil','Devinder','UmaSelvi']
}

df=pd.DataFrame(empdata)
print(df)
print(df.head(2))
print(df.tail(2))
print(df[2:5])


# In[ ]:




