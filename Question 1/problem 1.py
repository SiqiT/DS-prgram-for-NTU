#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
1.Operations for the right sum
Given a m x n matrix, we want to connect from top left corner (starting point, first row, first column) to
bottom right corner (ending point, mth row, nth column). Only 2 operations are allowed: Right (R) or Down
(D). Numbers that are passed through will be summed up. Given any summed number, you are required to
find out the operations needed to get the number.
a. For m=9, n=9 matrix, find the operations for the following summed numbers: 65, 72, 90, 110.
b. For m=90,000, n=100,000 matrix (90,000 rows, 100,000 columns), find the operations for the following
summed numbers: 87127231192 and 5994891682.

Method: For each summed number, construct a successful path and return it.
This program is running under Jupyter,python 2.7.
'''
import pandas as pd
import numpy as np

#Given a m x n matrix, summed number(SumNum), construct a successful path and return it.
#If no path exists for the given condition, return 0 and print 'No operation can get this summed number' on console.
def FindSteps(m,n,SumNum):
    StepNum = m+n-2L
    Path = ['0']*StepNum
    ColY = (1L+m)*m/2
    SumNow = SumNum-ColY
    RStepsNum = n-1L
    DStepsNum = m-1L
    DSteps1 = SumNow//(n-1)-1L
    RSteps2 = SumNow%(n-1)
    RSteps1 = RStepsNum-RSteps2
    if(RSteps2>0):
        DSteps2 = 1L
    else:
        DSteps2 = 0
    DSteps3 = DStepsNum-DSteps2-DSteps1
    if (DSteps3<0):
        Path = 0
        return Path
    for i in range(DSteps1):
        Path[i] = 'D'
    for i in range(DSteps1, RSteps1+DSteps1):
        Path[i] = 'R'
    if(DSteps2==1):
        Path[RSteps1+DSteps1] = 'D'
        for i in range(RSteps1+DSteps1+1, RSteps1+DSteps1+1+RSteps2):
            Path[i]= 'R'
    for i in range(RSteps1+DSteps1+DSteps2+RSteps2,StepNum):
        Path[i]= 'D'
    return Path  

def PrintPath(df1,SumNum,N,m,n):
    for i in range(N):
        steps = FindSteps(m,n,SumNum[i])
        if (steps != 0):
            StepsStr= ''.join(steps)
            new = pd.DataFrame({'SumNum':SumNum[i],
                            'Path':StepsStr},index=[i]  ) 
            df1 = df1.append(new,ignore_index=True)
        else:
            StepsStr = 'No operation can get this summed number'
    order = ['SumNum','Path']
    df1 = df1[order]
    return df1
    
#for question(a)
df1 = pd.DataFrame(columns = ['SumNum','Path']) 
SumNum = [65,72,90,110]
N = len(SumNum)
m = 9
n = 9
df1 = PrintPath(df1,SumNum,N,m,n)

#for question(b)
df2 = pd.DataFrame(columns = ['SumNum','Path']) 
SumNum = [87127231192,5994891682]#0~1
m = 90000
n = 100000
N = len(SumNum)
df2 = PrintPath(df2,SumNum,N,m,n)

df = pd.concat([df1,pd.DataFrame([[np.NaN]*2],columns = df1.columns),df2],ignore_index=True)    
df.to_csv( 'output_question_1',header = False,index=False,sep=' ')


# In[ ]:





# In[ ]:




