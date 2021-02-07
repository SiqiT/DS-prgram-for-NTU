#!/usr/bin/env python
# coding: utf-8

# In[27]:


'''
7.Coordinates-to-index & Index-to-coordinates
7.1 2-dimension
b) Given 2-dimensional grid with sizes (L1, L2) = (50, 57)
7.2 d-dimension
b) Given 6-dimensional grid with sizes 
(L1, L2, L3, L4, L5, L6)=(4, 8, 5, 9, 6, 7)

This program is running under Jupyter, python 2.7.
'''
import numpy
import pandas

#index
def CoordinateToIndex(x1,x2,L):
    I = L*x2+x1
    return I


# In[28]:


input_coordinates_7_1 = pandas.read_csv('input_coordinates_7_1.txt',sep='\t')
L = [50,57] 
n = len(L)
row = input_coordinates_7_1.shape[1] #6
col = input_coordinates_7_1.shape[0]
I = numpy.zeros([col,row])
X = input_coordinates_7_1.iloc[:, 1]
k = 0
for i in range(1,0,-1):
    x2 = X
    x1 = (input_coordinates_7_1.iloc[:, i-1]).values
    X = CoordinateToIndex(x1,x2,L[i-1])
index = X.to_frame()
index.rename(columns={'x2':'index'},inplace=True)
#print(index)
index.to_csv( 'output_index_7_1.txt',index=False)

input_index_7_1 = pandas.read_csv('input_index_7_1.txt',sep='\t') 
index = input_index_7_1.values
col = input_index_7_1.shape[0] #30240
I0 = numpy.zeros(col)
X = numpy.zeros((col,n))
for i in range(col):
    I0[0] = index[i]
    X[i,0] = I0[0]%L[0]
    I0[1] = I0[0]//L[0]
    X[i,1] = I0[1]%L[1]
X = X.astype(numpy.int16)
X = pandas.DataFrame(X)
X.columns = ['x1','x2']

X.to_csv( 'output_coordinates_7_1.txt',index=False,sep='\t')


# In[29]:


input_coordinates_7_2 = pandas.read_csv('input_coordinates_7_2.txt',sep='\t')
L = [4,8,5,9,6,7] #L5 = 7
n = len(L)
row = input_coordinates_7_2.shape[1] #6
col = input_coordinates_7_2.shape[0]
I = numpy.zeros([col,row])
X = input_coordinates_7_2.iloc[:, 5]
k = 0
for i in range(5,0,-1):#543210
    x2 = X
    x1 = (input_coordinates_7_2.iloc[:, i-1]).values
    X = CoordinateToIndex(x1,x2,L[i-1])
index = X.to_frame()
index.rename(columns={'x6':'index'},inplace=True)
index.to_csv( 'output_index_7_2.txt',index=False)

input_index_7_2 = pandas.read_csv('input_index_7_2.txt',sep='\t') 
index = input_index_7_2.values
col = input_index_7_2.shape[0] #30240
I0 = numpy.zeros(col)
X = numpy.zeros((col,n))
for i in range(col):
    I0[0] = index[i]
    X[i,0] = I0[0]%L[0]
    for j in range(1,6,1):
        I0[j] = I0[j-1]//L[j-1]
        X[i,j] = I0[j]%L[j]
X = X.astype(numpy.int16)
X = pandas.DataFrame(X)
X.columns = ['x1','x2','x3','x4','x5','x6']
X.to_csv( 'output_coordinates_7_2.txt',index=False,sep='\t')


# In[ ]:




