#!/usr/bin/env python
# coding: utf-8
Numpy_Assignment_2::
Question:1
Convert a 1D array to a 2D array with 2 rows?
# In[2]:


import numpy as np


# In[5]:


arr =np.arange(0,10)

arr.reshape(2,5)

Question:2
How to stack two arrays vertically?
# In[7]:


arr1=np.arange(10).reshape(2,5)
arr2 = np.ones(10 , dtype=int).reshape(2,5)
print(arr1,arr2)
np.vstack((arr1,arr2))

Question:3
How to stack two arrays horizontally?
Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1], [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[10]:


arr3=np.arange(10).reshape(2,5)
arr4 = np.ones(10 , dtype=int).reshape(2,5)

np.hstack((arr3,arr4))

Question:4
How to convert an array of arrays into a flat 1d array?
Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[15]:


arr5=np.array([[0,1,2,3,4],[5,6,7,8,9]])
arr5.flatten()

Question:5
How to Convert higher dimension into one dimension?
Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[17]:


arr6=np.arange(15).reshape(1,3,5)
print(arr6.ndim,"Dimension")
print(arr6)
arr6=arr6.flatten()
print(arr6.ndim,"Dimension")
arr6

Question:6
Convert one dimension to higher dimension?
Desired Output::
array([[ 0, 1, 2], [ 3, 4, 5], [ 6, 7, 8], [ 9, 10, 11], [12, 13, 14]])
# In[19]:


arr7=np.arange(15).reshape(-1,3)
arr7

Question:7
Create 5x5 an array and find the square of an array?
# In[20]:


arr8 = np.arange(25).reshape(5,5)
print(arr8)
np.square(arr)


# Question:8
# Create 5x6 an array and find the mean?

# In[21]:


np.random.seed(123)
arr9=np.random.randint(30,size=(5,6))
print(arr9)
arr9.mean()

Question:9
Find the standard deviation of the previous array in Q8?
# In[22]:


np.random.seed(123)
arr10=np.random.randint(30,size=(5,6))
print(arr10)


# In[23]:


np.std(arr)

Question:10
Find the median of the previous array in Q8?¶
# In[26]:


np.random.seed(123)
arr11=np.random.randint(30,size=(5,6))
print(arr11)
np.median(arr11)

Question:11
Find the transpose of the previous array in Q8?
# In[27]:


np.random.seed(123)
arr12=np.random.randint(30,size=(5,6))
print(arr12)


# In[28]:


arr12.T


#  Question:12
# Create a 4x4 an array and find the sum of diagonal elements?

# In[34]:


arr13 = np.arange(16).reshape(4,4)
print(arr13)
np.diagonal(arr13)


# Question:13
# Find the determinant of the previous array in Q12?

# In[36]:


arr13 = np.arange(16).reshape(4,4)
print(arr13)
np.linalg.det(arr13)


# Question:14
# Find the 5th and 95th percentile of an array?

# In[40]:


arr14=np.arange(10)
print(arr14)
print(np.percentile(arr14,5))
print(np.percentile(arr14,95))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




