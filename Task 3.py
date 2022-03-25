#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Write a Python program to count the number of characters (character frequency) in a string.
# 
# Examble: ('google.com') =>  {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# 

# In[1]:


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))


# # Question  2

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

Examble => 'restart' => 'resta$t'
           'google'  => 'goo$le'
# In[2]:


def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))


# # Question 3
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Examble : 'abc', 'xyz' => xyc abz
# In[3]:


def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


# # Question 4
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Examble => ab => ab
        => abc => abcing 
        => string => stringly
# In[10]:


def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))


# # Question 5

# Write a Python script to display the various Date Time formats.
# 
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
# Solution=>
# import time
# import datetime

# In[11]:


import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))


# # Question 6

# Write a Python program to print yesterday, today, tomorrow.
# 
# Yesterday :  2020-01-17
# Today :  2020-01-18
# Tomorrow :  2020-01-19
# Solution=>
# import datetime

# In[12]:


import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)


# # Question 7

# 
# Write a Python program to add 5 seconds with the current time.
# 
# 
# Current time=> 13:09:38.491219
# After 5 seconds => 13:09:43.491219

# In[17]:



import datetime
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())


# # Question 8

# In[ ]:


Write a Python program to convert Year/Month/Day to Day of Year.


# In[18]:


import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)


# # Question 9
Write a Python program to get current time in milliseconds.
# In[19]:


import time
milli_sec = int(round(time.time() * 1000))
print(milli_sec)


# # Question 10
Write a Python program to get week number.
# In[21]:


import datetime
print(datetime.date(2022, 3, 25).isocalendar()[1])


# # Question 11
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# In[22]:


import re
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))


# # Question 12

# In[ ]:




Write a Python program to calculate the area of a trapezoid.
# In[ ]:





# In[27]:


height = float(input("Height of trapezoid: "))


# In[28]:


base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))


# In[29]:


area = ((base_1 + base_2) / 2) * height
print("Area is:", area)


# In[ ]:




