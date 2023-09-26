#!/usr/bin/env python
# coding: utf-8

# **Chapter 9**

# In[19]:


eng2sp = dict()
print(eng2sp)


# In[3]:


type(eng2sp)


# In[5]:


eng2sp['one'] = 'uno'
print(eng2sp)


# In[20]:


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp)


# In[8]:


eng2sp['two']


# In[9]:


eng2sp['four']


# In[10]:


len(eng2sp)


# In[11]:


'one' in eng2sp


# In[12]:


'uno' in eng2sp


# In[14]:


vals = list(eng2sp.values())
# print(vals)
'uno' in vals


# In[21]:


word = 'brontosaurus' 
d = dict()
for c in word:
    if c not in d: 
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)


# In[16]:


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}


# In[17]:


type(counts)


# In[18]:


print(counts.get('jan', 0))


# In[19]:


print(counts.get('tim', 0))


# In[20]:


print(counts)


# In[1]:


word = 'brontosaurus' 
d = dict()
for c in word:
    d[c] = d.get(c,0) + 2 
print(d)


# In[24]:


fname = input('Enter the file name: ') 

try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    exit()
    
counts = dict() 
for line in fhand:
    words = line.split() 
    #print(words)
    for word in words:
        if word not in counts: 
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)


# In[3]:


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100} 
for key in counts:
    print(key, counts[key])


# In[4]:


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100} 
for key in counts:
    if counts[key] > 10 : 
        print(key, counts[key])


# In[6]:


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100} 
lst = list(counts.keys())
print(lst)
lst.sort()
print(lst)


# In[7]:


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100} 
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])


# In[12]:


jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))


# In[13]:


print(jjj.keys())


# In[14]:


print(jjj.items())


# In[15]:


jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for aaa,bbb in jjj.items() : # it items method return key and value. Therefore, we need to variables.
    print(aaa, bbb)


# In[18]:


name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


# In[25]:


import string
string.punctuation


# In[10]:


import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)


# In[2]:


word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 2
print(d)


# In[ ]:




