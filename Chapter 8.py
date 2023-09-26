#!/usr/bin/env python
# coding: utf-8

# **Chapter 8**

# In[1]:


print([1, 24, 76])


# In[2]:


print(['red', 'yellow', 'blue'])


# In[3]:


print(['red', 24, 98.6])


# In[4]:


print([1, [5,6], 7])


# In[5]:


print([])


# In[7]:


for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')


# In[8]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')


# In[9]:


friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])


# In[10]:


fruit = 'Banana'
fruit[0] = 'b'


# In[11]:


x = fruit.lower()
print(x)


# In[12]:


print(fruit)


# In[13]:


lotto = [2, 14, 26, 41, 63]
print(lotto)


# In[14]:


lotto[2] = 28
print(lotto)


# In[15]:


greet = 'Hello Bob'
print(len(greet))


# In[17]:


x = [1, 2, 'joe', 99]
print(len(x))


# In[18]:


print(range(4))


# In[19]:


friends = ['Joseph', 'Glenn', 'Sally']
print(range(len(friends)))


# In[20]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)


# In[21]:


friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:', friend)


# In[23]:


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


# In[24]:


t = [9, 41, 12, 3, 74, 15]
t[1:3]


# In[25]:


t[:4]


# In[26]:


t[3:]


# In[27]:


t[:]


# In[29]:


x  = list()
type(x)


# In[30]:


dir(x)


# In[36]:


stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)


# In[37]:


stuff.append('cookie')
print(stuff)


# In[38]:


some = [1, 9, 21, 10, 16]
9 in some


# In[39]:


15 in some


# In[40]:


20 not in some


# In[41]:


friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)


# In[42]:


print(friends[1])


# In[43]:


nums = [3, 41, 12, 9, 74, 15]
print (len(nums))


# In[44]:


print(max(nums))


# In[45]:


print(min(nums))


# In[46]:


print(sum(nums))


# In[47]:


print(sum(nums)/len(nums))


# In[2]:


total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
    
average = total / count
print('Average: ', average)


# In[4]:


numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)    


# In[5]:


[1,2,3] * 4


# In[14]:


t = [3, 2, 1]
t.sort()
print(t)
t = t.sort()
print(t)


# In[15]:


fhand = open('mbox-short.txt') 
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue 
    words = line.split()
    print(words[2])


# In[11]:


fhand = open('mbox-short.txt') 
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue 
    words = line.split()
    email = words[1]
    pieces = email.split('@') 
    print(pieces[1])


# In[12]:


t = list()
type(t)


# In[13]:


dir(t)


# In[ ]:


s = "Hello World       Palistan"

