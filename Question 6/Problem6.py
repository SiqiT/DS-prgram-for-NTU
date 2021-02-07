#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
6.Points inside/outside polygon
Given a sequence of points that form a polygon, you are required to tell if a list of points are either inside or
outside the polygon.

Method: Build a Scan-Line Algorithm, 
Calculate the intersection number for each points' scan line(y=point.Y) with the given polygon,
only consider about the intersection on the point's right side
if the number is odd, then this point is inside the polygon
if the number is even, this point is outside the polygon
This program is running under Jupyter, python 2.7.
'''
import numpy
import matplotlib.pyplot as plt
import pandas
input_question_6_points = pandas.read_csv('input_question_6_points',sep=' ',header=-1) 
input_question_6_polygon=pandas.read_csv('input_question_6_polygon',sep=' ',header=-1) 
#PolygonPoints = [[1,1],[1,5],[10,5],[10,1]]
#PolygonPoints =[[4,3],[2,6],[3,12],[2,17],[5,20],[9,21],[14,19],[20,14],[18,3],[11,7]]
#Points = [[7,11],[10,14],[11,4],[12,21],[16,3],[16,10],[17,4],[18,7],[18,17],[20,7]]
PolygonPoints = numpy.array(input_question_6_polygon)
Points = numpy.array(input_question_6_points)
PolygonPoints = numpy.array(PolygonPoints)
#Points = numpy.array(Points)
N = len(PolygonPoints)
P = len(Points)
p1 = PolygonPoints[0] #p1 is a vertex of polygon
results = ['0']*P

#point i in the polygon or not
for i in range(P):
    ans = 0
    intersectNum = 0
    for j in range(N):# point i's relationship with Polygon's vertex j or edge j
        #if point i is polygon's vertex
        if((Points[i]==p1).all()):   
            results[i] = "inside"
            ans = 1
            break
        p2 = PolygonPoints[(j+1) % N]
        #if scan-line i has no intersection with Polygon's edge j
        if (Points[i,1]<min(p1[1],p2[1]) or Points[i,1]> max(p1[1],p2[1])): 
            p1 = p2
            continue
        #if polygon's edge j is horizontal and scan-line i is on edge j
        if(p1[1]== p2[1] and Points[i,1]==p1[1]): 
            #point i is on edge j
            if( Points[i,0] >= min(p1[0],p2[0]) and Points[i,0]<=max(p1[0],p2[0])):
                results[i] = 'inside'
                ans = 1
                break
            else:
                p1 = p2
                continue
        #scan-line i only intesect with a polygon's vertex j
        if(Points[i,1]==p1[1] and Points[i,0]<p1[0]): #在顶点左边
            p3 = PolygonPoints[(j+N-1) % N]
            #if two polygon's edges which through vertex j are on the different side of scan-line i , 
            #then intesection num + 1
            if(Points[i,1] > min(p2[1], p3[1]) and Points[i,1] < max(p2[1], p3[1])):
                intersectNum = intersectNum+1
            #if two polygon's edges which through vertex j are on the same side of scan-line i , 
            #then intesection num + 2
            else:
                intersectNum = intersectNum+2
        #if scan-line i is intersect with edge j, find the intersection point       
        if (Points[i,1]>min(p1[1],p2[1]) and Points[i,1]< max(p1[1],p2[1])): 
            XonLine=(Points[i,1]-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
            #if the intersect point is point i
            if(abs(Points[i,0]-XonLine)<0.00001):
                results[i] = 'inside'
                ans = 1
                break
            #if the intersection point is not point i and the intetrsection point is on the right side
            #then intesection num +1
            elif(Points[i,0]<XonLine):#点在线左边
                intersectNum = intersectNum+1       
        p1 = p2
    
    #if intersection(intersectNum) num is even, the point is outside the polygon
    if(intersectNum % 2 == 0 and ans==0):
        results[i] = 'outside'
        continue
    #if intersection(intersectNum) num is odd, the point is inside the polygon
    elif(intersectNum % 2 != 0 and ans==0):
        results[i] = "inside"
        continue
        
#PolygonPoints1 = [[4,3],[2,6],[3,12],[2,17],[5,20],[9,21],[14,19],[20,14],[18,3],[11,7],[4,3]]
#PolygonPoints1 = [[1,1],[1,5],[10,5],[10,1],[1,1]]
#PolygonPoints1 = pandas.DataFrame(PolygonPoints1)
#print(PolygonPoints[1])        
#plt.plot(PolygonPoints1[0],PolygonPoints1[1], '.-')  
#for i in range(P):
#    plt.plot(Points[i,0], Points[i,1], '.r')
#plt.show()             
df1 = pandas.DataFrame(columns = ['x','y','results'])
df1['x'] = Points[:,0]
df1['y'] = Points[:,1]
df1['results'] = results
df1.to_csv( 'output_question_6',header = False,index=False,sep=' ')


# In[ ]:





# In[ ]:




