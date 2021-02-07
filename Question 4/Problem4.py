#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
4.Connected components
Write a code to find out connected components for a given image. When a group of pixels in the image is
“connected” to each other, they are said to form a connected cluster and we refer to this cluster as connected
component. In imaging, pixels can be connected in 4 neighbors (4-connectivity) or 8 neighbors (8-connectivity).
In the example given below, the input image will result in 3 connected components if using 4-connectivity or
2 connected components if using 8-connectivity. You can implement either 4-connectivity or 8-connectivity
connected components.

Method: Build a recursive Seed-Filling Algorithm(4-connectivity)
This program is running under Jupyter, python 2.7.
'''
import pandas
import numpy
input_image = pandas.read_csv('input_question_4',sep='\t',header=None)
input_image = input_image.values
#print(input_image)
m = len(input_image[:,1])#row
n = len(input_image[1,:])#column

#In order to mark connected component from number 1, change pixels value from 1 to -1 first.
for j in range(n):
    for i in range(m):
        if (input_image[i,j] == 1):
            input_image[i,j] = -1
#print(input_image)

example = numpy.array([[0,0,1,1],[1,1,0,0],[0,0,0,0], [0,1,1,0],[0,1,1,1]])
m0 = 5
n0 = 4
label = 1

#for a given image s, 0 represents background, -1 represents foreground, 
#for a seed pixel(s[i,j]), find its connected component and label it as index
def Fill(s,i,j,index):
    if (s[i,j]==-1):
        #first label seed s[i,j] as index
        s[i,j] = index
        #searching its' 4-connectivity pixels, 
        #if one of them is foreground, recursive searching its' connected component and label it.
        if(i-1>=0 and s[i-1,j]==-1):
            Fill(s,i-1,j,index)
        if(i+1<=m-1and s[i+1,j]==-1):
            Fill(s,i+1,j,index)
        if(j-1>=0 and s[i,j-1]==-1):
            Fill(s,i,j-1,index)
        if(j+1<=n-1and s[i,j+1]==-1):
            Fill(s,i,j+1,index)
    return

#find seeds, for each seed, using Seed-Filling Algorithm(Fill(s,i,j,index)) label connected components.
for j in range(n):
    for i in range(m):
        if (input_image[i,j]==-1):
            Fill(input_image,i,j,label)
            label = label+1
#print(input_image)
#print(type(input_image))
a = pandas.DataFrame(input_image)
#print(a)
a.to_csv('output_question_4', sep=' ',index=False,header=None)


# In[ ]:





# In[ ]:





# In[ ]:




