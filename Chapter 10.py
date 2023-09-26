#!/usr/bin/env python
# coding: utf-8

# **Chapter 10**

# In[1]:


x = ('Glenn', 'Sally', 'Joseph')
print(x[2])


# In[2]:


y = ( 1, 9, 2 )
print(y)


# In[3]:


print(max(y))


# In[4]:


for iter in y:
    print(iter)


# In[6]:


x = [9, 8, 7]
print(x)
x[2] = 6
print(x)


# In[7]:


y = 'ABC'
y[2] = 'D'


# In[8]:


z = (5, 4, 3)
z[2] = 0


# In[23]:


x = (3, 2, 1)
x.sort()


# In[24]:


x.append(5)


# In[25]:


x.reverse()


# In[26]:


l = list()
dir(l)


# In[27]:


t = tuple()
dir(t)


# In[ ]:


(x, y) = (4, 'fred')
print(y)


# In[ ]:


(a, b) = (99, 98)
print(a)


# In[9]:


d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items(): 
    print(k, v)


# In[10]:


tups = d.items()
print(tups)


# In[ ]:


(0, 1, 2) < (5, 1, 2)


# In[ ]:


(0, 1, 2000000) < (0, 3, 4)


# In[ ]:


( 'Jones', 'Sally' ) < ('Jones', 'Sam')


# In[ ]:


( 'Jones', 'Sally') > ('Adams', 'Sam')


# In[11]:


d = {'a':10, 'b':1, 'c':22}
d.items()


# In[ ]:


sorted(d.items())


# In[12]:


d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
t


# In[13]:


type(t)


# In[14]:


for k, v in sorted(d.items()):
    print(k, v)


# In[16]:


c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append((v, k))
print(tmp)


# In[17]:


tmp = sorted(tmp, reverse=True)
print(tmp)


# In[1]:


fhand = open('romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items():
    newtup = (val, key) 
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
 print(key, val)


# In[ ]:





# In[21]:


c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )


# In[ ]:


fhand = open('romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items():
    newtup = (val, key) 
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
 print(key, val)

