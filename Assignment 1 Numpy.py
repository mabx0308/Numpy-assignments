#!/usr/bin/env python
# coding: utf-8

# #Import the numpy package under the name np

# In[1]:


import numpy as np


# Create a null vector of size 10

# In[2]:


vector=np.zeros(10)
print(vector)


# Create a vector with values ranging from 10 to 49

# In[3]:


vector=np.arange(10,49)
print(vector)


# Find the shape of previous array in question 3

# In[4]:


print(np.shape(vector))


# Print the type of the previous array in question 3

# In[5]:


vector.dtype


# Print the numpy version and the configuration

# In[6]:


print(np.__version__)
np.show_config()


# Print the dimension of the array in question 3

# In[7]:


vector.ndim


# Create a boolean array with all the True values

# In[8]:


a=np.random.rand((8))


# In[9]:


print(a)


# In[10]:


a>0


# Create a two dimensional array
# 

# In[11]:


np.ones((2,2))


# Create a three dimensional array

# In[12]:


np.ones((3,3))


# Difficulty Level Easy
# 
# Reverse a vector (first element becomes last)

# In[13]:


x=np.arange(20)


# In[14]:


x[4]


# In[15]:


x=x[::-1]
print(x)


# Create a null vector of size 10 but the fifth value which is 1

# In[16]:


z=np.zeros((10))
print(z)


# In[17]:


z[5]=1


# In[18]:


print(z)


# Create a 3x3 identity matrix

# In[19]:


np.ones((3,3))


# arr = np.array([1, 2, 3, 4, 5])
# Convert the data type of the given array from int to float

# In[20]:


arr=np.array([1,2,3,4,5])


# In[21]:


arr.astype("float64")


# Multiply arr1 with arr2

# In[22]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])  

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

m=arr1*arr2


# In[23]:


print(m)


# arr1 = np.array([[1., 2., 3.],
# 
#             [4., 5., 6.]]) 
# 
# arr2 = np.array([[0., 4., 1.],
# 
#             [7., 2., 12.]])
# Make an array by comparing both the arrays provided above
# 
# 

# In[24]:


arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])


# In[25]:


arr3=np.concatenate((arr1,arr2))
arr3


# Extract all odd numbers from arr with values(0-9)

# In[26]:


k=np.arange(10)
k


# In[27]:


k[1:10:2]


# Replace all odd numbers to -1 from previous array

# In[28]:


k[1:10:2]=-1
k


# arr = np.arange(10)
# Replace the values of indexes 5,6,7 and 8 to 12

# In[29]:


arr = np.arange(10)
arr


# Create a 2d array with 1 on the border and 0 inside

# In[30]:


array=np.arange(0,9)
array.reshape(3,3)


# In[31]:


array[0]


# Difficulty Level Medium
# 
# arr2d = np.array([[1, 2, 3],
# 
#             [4, 5, 6], 
# 
#             [7, 8, 9]])
# Replace the value 5 to 12

# In[32]:


arr2d = np.array([[1, 2, 3],

        [4, 5, 6], 

        [7, 8, 9]])
arr2d


# In[33]:


arr2d[1][1]=12
arr2d


#  arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# Convert all the values of 1st array to 64

# In[35]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) 
arr3d


# Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[36]:


arr6=np.arange(0,9)
arr6.reshape(3,3)


# Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[37]:


arr7=np.arange(0,9).reshape(3,3)
arr7


# In[38]:


arr7[1,1]


# Create a 10x10 array with random values and find the minimum and maximum values

# In[41]:


arr8=np.random.randint(100,size=(10,10))
arr8


# In[42]:


print(np.min(arr8))
print(np.max(arr8))


# a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# Find the common items between a and b

# In[43]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8]) 


# In[45]:


r=np.intersect1d(a,b)
r


# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# Find all the values from array data where the values from array names are not equal to Will

# In[51]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
data


# In[53]:


data[names!= "Will"]


# Find all the values from array data where the values from array names are not equal to Will and Joe

# In[55]:


data[names!= "Will"]
data[names!= "Joe"]


# Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[56]:


arr9=np.random.randn(1,15).reshape(5,3)
arr9


# Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[57]:


arr10=np.random.randn(1,16).reshape(2,2,4)
arr10


# Swap axes of the array you created in Question 32

# In[58]:


arr10.T


# Find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[60]:


R=np.arange(10)
R=np.sqrt(R)
np.where(R<0.5,0,R)


# Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[61]:


a=np.random.randint(12)
b=np.random.randint(12)
np.maximum(a,b)


# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# Find the unique names and sort them out

# In[62]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names


# In[65]:


names=set(names)
names


# x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# Find the dot product of the above two matrix

# In[66]:


x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
prod=(np.dot(x,y))
prod


# Generate a matrix of 20 random values and find its cumulative sum

# In[67]:


matrix=np.random.random(20)
matrix


# In[70]:


sum=np.cumsum(matrix)
sum


# In[ ]:





# In[ ]:





# In[ ]:




