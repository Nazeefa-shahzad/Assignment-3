#!/usr/bin/env python
# coding: utf-8

# **Chapter 7**

# In[1]:


#Opening a File using open()

fhand = open('mbox.txt')
print(fhand)


# In[2]:


#When Files are Missing

fhand = open('stuff.txt')


# In[ ]:


# The newline Character - \n its a single character not two
stuff = 'Hello\nWorld!'
stuff


# In[ ]:


print(stuff)


# In[ ]:


stuff = 'X\nY'
print(stuff)


# In[ ]:


len(stuff)


# In[ ]:


# File Processing - A text file can be thought of as a sequence of lines

xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)


# In[ ]:


fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)


# In[ ]:


#Reading the *Whole* File - We can read the whole file (newlines and all) into a single string
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))


# In[ ]:


# Slicing Strings

print(inp[:20])


# In[ ]:


# Searching Through a File

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line)


# In[ ]:


# Searching Through a File (fixed)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line[6:])


# In[ ]:


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)


# In[ ]:


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line[6:])
        


# In[ ]:


#Using in to Select Lines

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)


# In[ ]:


fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
#Prompt for File Name
print('There were', count, 'subject lines in', fname)


# In[ ]:


fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

