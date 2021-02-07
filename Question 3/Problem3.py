#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
3. Multilayer perceptron for regression
In this question, you are given a training dataset that consists of three independent variables x1, x2, x3 and a
dependent variable y=f(x1, x2, x3). You are required to construct the Multi Layer Perceptron (MLP) model
shown in Figure 3 to predict the dependent variable y by using the values of independent variables x1, x2 and
x3. After constructing and training the MLP model with training dataset, you will predict the values of y for
the test dataset.

Method: For this question, I construct a MLPRegressor from sklearn and use this model to predict y.
This program is running under Jupyter, python 2.7
'''
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


train_data = pd.read_csv('train_data.txt',sep='\t') #10000*3
train_truth =  pd.read_csv('train_truth.txt',sep='\t')
test_data =  pd.read_csv('test_data.txt',sep='\t')


# '''build new verified sets and train sets, to get the best parameters for a MLPRegressor
# train1 = train_data.iloc[0:800,:]
# truth1 = train_truth.iloc[0:800,:]
# testTrain = train_data.iloc[801:1000,:]
# testTruth = train_truth.iloc[801:1000,:]
# 
# ss = StandardScaler()
# X_train = ss.fit_transform(train1)
# X_test = ss.fit_transform(testTrain)
# Y_train = truth1
# Y_test = testTruth
# 
# fit1 = MLPRegressor(hidden_layer_sizes=(4,4), activation='relu',solver='lbfgs',alpha=0.01)
#         #4*4, with those parameters above can get a smallest error.
# 
# fit1.fit(X_train,Y_train)
# print ("fitting model right now")
# pred1_train = fit1.predict(X_train)
# 
# #calculate training set mean_squared_error
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import explained_variance_score
# from sklearn.metrics import r2_score
# r2_1 = r2_score(Y_train, pred1_train)
# evs_1 = explained_variance_score(Y_train, pred1_train)
# mse_1 = mean_squared_error(pred1_train,Y_train)
# print("r2 train = ", r2_1)
# print("explained_variance train = ", evs_1)
# print ("Train ERROR = ", mse_1)
# 
# #calculate testing set mean_squared_error
# pred1_test = fit1.predict(X_test)
# r2_2 = r2_score(pred1_test,Y_test)
# evs_2 = explained_variance_score(pred1_test,Y_test)
# mse_2 = mean_squared_error(pred1_test,Y_test)
# print("r2 test = ", r2_2)
# print("explained_variance test= ", evs_2)
# print ("Test ERROR = ", mse_2)
# '''
# 

# In[8]:


ss = StandardScaler()
train_data = ss.fit_transform(train_data)
test_data = ss.fit_transform(test_data)
fit2 = MLPRegressor(hidden_layer_sizes=(4,4), activation='relu',solver='lbfgs',alpha=0.01)

fit2.fit(train_data,train_truth)
print ("fitting model right now")
test_predicted = fit2.predict(test_data)
test_predicted = pd.DataFrame(test_predicted)
test_predicted.columns = ['y']
#print(test_predicted)
test_predicted.to_csv('test_predicted.txt', sep='\t',index=False)
print ("Prediction finished.")


# In[ ]:





# In[ ]:




