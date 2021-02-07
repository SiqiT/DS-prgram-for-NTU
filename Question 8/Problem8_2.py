#!/usr/bin/env python
# coding: utf-8

# In[82]:


'''8.2
Write a code to numerically solve these four equations using the fourth-order RungeKutta method. For this exercise, assume that the initial concentration of E is 1 µM, the 
initial concentration of S is 10 µM, and the initial concentrations of ES and P are both 0. The
rate constants are: k1=100/µM/min, k2=600/min, k3=150/min.

This program is running under Jupyter， python 2.7, python 2.7.
'''
import math
import numpy as np
import matplotlib.pyplot as plt

k1=100.0    
k2=600.0   #/(60*1000)  
k3=150.0   #/(60*1000)  
E0=1.0     #/1000  
PointNum=5000
S=np.zeros(PointNum)
ES=np.zeros(PointNum)
P=np.zeros(PointNum)
E=np.zeros(PointNum)
V=np.zeros(PointNum)
V[0]=0.0
S[0]=10.0    #/1000   
ES[0]=0.0
P[0]=0.0
E[0]=E0
h=4.0/(60*1000) #4ms   
t=np.zeros(PointNum)
t[0]=0
km=(k2+k3)/k1  # 
for i in range(1,PointNum):
    Kp1=k3*ES[i-1]    
    Kes1=k1*(E0-ES[i-1])*S[i-1]-(k2+k3)*ES[i-1]   
    Ks1=k2*ES[i-1]-k1*(E0-ES[i-1])*S[i-1]
    
    Kp2=k3*(ES[i-1]+0.5*h*Kes1)
    Kes2=k1*(E0-(ES[i-1]+0.5*h*Kes1))*(S[i-1]+0.5*h*Ks1)-(k2+k3)*(ES[i-1]+0.5*h*Kes1)
    Ks2=k2*(ES[i-1]+0.5*h*Kes1)-k1*(E0-(ES[i-1]+0.5*h*Kes1))*(S[i-1]+0.5*h*Ks1)
    
    Kp3=k3*(ES[i-1]+0.5*h*Kes2)
    Kes3=k1*(E0-(ES[i-1]+0.5*h*Kes2))*(S[i-1]+0.5*h*Ks2)-(k2+k3)*(ES[i-1]+0.5*h*Kes2)
    Ks3=k2*(ES[i-1]+0.5*h*Kes2)-k1*(E0-(ES[i-1]+0.5*h*Kes2))*(S[i-1]+0.5*h*Ks2)
    
    Kp4=k3*(ES[i-1]+h*Kes3)
    Kes4=k1*(E0-(ES[i-1]+h*Kes3))*(S[i-1]+h*Ks3)-(k2+k3)*(ES[i-1]+h*Kes3)
    Ks4=k2*(ES[i-1]+h*Kes3)-k1*(E0-(ES[i-1]+h*Kes3))*(S[i-1]+h*Ks3)
    
    P[i]=P[i-1]+h/6.0*(Kp1+2*Kp2+2*Kp3+Kp4)
    ES[i]=ES[i-1]+h/6.0*(Kes1+2*Kes2+2*Kes3+Kes4)
    S[i]=S[i-1]+h/6.0*(Ks1+2*Ks2+2*Ks3+Ks4)
    E[i]=E0-ES[i]
    #if(abs(E[i]-ES[i])<0.001 ):
        #print(E[i],i)
    t[i]=t[i-1]+h
    #V[i]=k3*ES[i]
    V[i]=(k3*E0*S[i-1]/(S[i-1]+km))

plt.figure(1)
plt.xlim(0,0.01)
plt.ylim(0,1)
plt.plot(t, E, color='green', label='E')
plt.plot(t, ES, color='red', label='ES')
plt.xlabel(u"Time")
plt.ylabel(u"Concentration")
plt.legend()

plt.figure(2)
plt.xlim(0,0.12)
plt.ylim(0,10)
plt.plot(t, P,  color='skyblue', label='P')
plt.plot(t, S,  color='orange', label='S')
plt.xlabel(u"Time")
plt.ylabel(u"Concentration")
plt.legend() 


plt.figure(3)
plt.xlim(0,9)
plt.ylim(0,90)
plt.plot(S,V)
plt.xlabel(u"[S]")
plt.ylabel(u"Vo")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




