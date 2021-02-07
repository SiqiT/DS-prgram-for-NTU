#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
5. Coloring
Given a L by L square grid, consider 4 neighbors connections. Given L2 beads of different colors.
Put all the beads onto the grid and the penalty for putting any two beads of the same color as neighbor is one. 
Total penalty is the sum of all panelties. Your task is to find a way to put the beads onto the square grid with least
penalty. Perform this tasks with
1. L=5 with 12 red beads (R) and 13 blue beads (B)
2. L=64 with 139 red beads (R), 1451 blue beads (B), 977 green beads (G), 1072 white beads (W), 457
yellow beads (Y)

Method: From the upper left to the lower right, 
put each grid with the bead which has the largest number and a different color with its neighbor.
This program is running under Jupyter, python 2.7.
'''
import numpy
import pandas

R = 12
B = 13
n0 = 12 #n[0]
n1 = 13

#Given a L*L grid, put color(ColorNames) beads(n) onto the grid 
def coloring(L,n,ColorNames):
    ColorsNum = len(n)
    beads = numpy.zeros((L,L),dtype = int)
    index=0
    for i in range(L):
        for j in range(L):
            if(i==0 and j==0):
                color = findColor(n)
            elif (i==0 and j>0):
                color = findColor(n, -1, beads[i,j-1])
            elif (i>0 and j==0):
                color = findColor(n, beads[i-1,j], -1)
            else:
                color = findColor(n, beads[i-1,j], beads[i,j-1])
                
            if (color!=-1):
                beads[i,j] = color
                n[color] = n[color]-1
            
    return(beads)

#Find a color(maxColor) for current grid from color-beads-number array(colorBeads) 
#the color is different from its' left(LeftColor) and up(UpColor) neighbors
def findColor(colorBeads,UpColor=-1,LeftColor=-1):
    maxColor = -1
    maxColorNum = 0
    for i in range(len(colorBeads)):
        if (i!= UpColor and i!= LeftColor and colorBeads[i]>maxColorNum):
            maxColor = i
            maxColorNum = colorBeads[i]
    if(maxColor==-1):
        print('panelty')
        if(UpColor!=-1 and LeftColor!=-1):
            if(colorBeads[UpColor]>=colorBeads[LeftColor] and colorBeads[UpColor]>0):
                maxColor = UpColor
            elif (colorBeads[LeftColor]>0):
                maxColor = LeftColor
        elif(UpColor==-1 and LeftColor!=-1):
            if(colorBeads[LeftColor]>0):
                maxColor = LeftColor
        elif(UpColor!=-1 and LeftColor==-1):
            if(colorBeads[UpColor]>0):
                maxColor = UpColor
    return(maxColor)

ColorNames = ['R','B','G','W','Y']            
n = [139,1451,977,1072,457]
L = 64
Beads = coloring(L,n,ColorNames)
BeadsColorNames = numpy.zeros((L,L),dtype=str)
for i in range(L):
    for j in range(L):
        index = int(Beads[i,j])
        BeadsColorNames[i,j] = ColorNames[index]
BeadsColorNames = pandas.DataFrame(BeadsColorNames)
BeadsColorNames.to_csv( 'output_question_5_2',index=False,header = False,sep=' ')
#139 red beads (R), 1451 blue beads (B), 977 green beads (G), 1072 white beads (W), 457        


# In[2]:


ColorNames = ['R','B']            
n = [12,13]
L = 5
Beads = coloring(L,n,ColorNames)
BeadsColorNames = numpy.zeros((L,L),dtype=str)
for i in range(L):
    for j in range(L):
        index = int(Beads[i,j])
        BeadsColorNames[i,j] = ColorNames[index]
BeadsColorNames = pandas.DataFrame(BeadsColorNames)
#print(BeadsColorNames)
BeadsColorNames.to_csv( 'output_question_5_1',index=False,header = False,sep=' ')


# In[ ]:




