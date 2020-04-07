#!/usr/bin/env python
# coding: utf-8

# 1)Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#   of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#   comma-separated sequence on a single line.

# In[1]:


for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')


# 2) Write a Python program to accept the user's first and last name and then getting them printed in
#    the the reverse order with a space between first name and last name.

# In[2]:


Fname= input("Your First Name: ")
Lname= input("your Last name: ")
print ("Full Name is:" +Lname+" "+Fname)


# 3) Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[3]:


pi=22/7
d= float(input("diameter of sphere: "))
r=d/2
volume=4/3 * pi * r**3
volume=str(volume)
print ("Volume of Sphere is: "+volume)


# 4) Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[9]:


numbers=input("cs numbers: ")
List= list(numbers)
print (List)


# 6) Write a Python program to reverse a word after accepting the input from the user.

# In[11]:


word= input("input word: ")
print (word[::-1])


# 7) Write a Python Program to print the given string in the format specified in the sample output.

# In[16]:


string = "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{}and to secure to all its citizens{}"
print(string.format('\n\t','!\n\t\t','\n\t\t',':'))

