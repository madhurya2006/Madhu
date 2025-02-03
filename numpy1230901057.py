#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3,4,5])
print("one dimensional array:",a)


# In[2]:


import numpy as np
b=np.array([[10,20,30],[50,60,70]])
print("two dimensional array:",b)


# In[3]:


import numpy as np
x=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("three dimensional array:",x)


# In[4]:


import numpy as np
y=np.zeros((3,5))
print("\n array with all zeros:\n",y)


# In[5]:


import numpy as np
n=np.random.random((2,2))
print("\n Random values:\n",n)


# In[7]:


import numpy as np
m=np.arange(3,20,3)
print("\n Sequence array \n",m)


# In[8]:


import numpy as np
f=np.array([[1,2,3,4],[7,8,9,6],[0,11,50,32]])
g=f.reshape(4,3)
print("\n original array:\n",f)
print("\n reshaped array:\n",g)


# In[9]:


import numpy as np
p=np.array([[1,2,3],[4,5,6]])
flat=p.flatten()
print("\n original array:\n",p)
print("flattened array:",flat)


# In[14]:


print("\n No.Of.Dimensions:\n",p.ndim)


# In[17]:


import numpy as np
o=np.array([5,6,7,8,9,0])
print("no.of.dimensions:",o.ndim)


# In[23]:


import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("no.of dimensions:",a.ndim)


# In[24]:


import numpy as np
b=np.array([[1,2,3],[4,5,6]])
print("shape of the array:",b.shape)


# In[25]:


print("\n Array element type:",b.dtype)


# In[26]:


size=len(b)
print("\n size of the array:\n",size)


# In[31]:


import numpy as np
c=np.array([1,2,3,4])
size=len(c)
print("size of array:",c.size)


# In[ ]:





# In[ ]:




