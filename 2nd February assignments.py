#!/usr/bin/env python
# coding: utf-8

# ##  Q1.what are the characterstics of tuples? Is tuples immutable?

#  #### A tuples is an ordered , immutable collection of the elements of any data type. Here are some key characterstics of tuples:
# 
# 1. Ordered: Tuples are ordered,it means that the elements in tuple have a specific order, and that order is maintained.
# 
# 2. Immutable: Tuples are immutable,it means that once a tuple is created,its content cannot be changed. It is not possible to add,remove or modify elements of tuple. However,it is possible to create a new tuple that contains some or all of the elements of the original tuple,or to convert a tuple to a list and then modify the list.
# 
# 3. Heterogeneous: Tuples can contain all the elements of different data types. For example, a tuple can contain  integers,strings,and other tuples.
# 
# 4. Accessible by index : Individual elements of tuple can be accessed by their index of 0,the secod element has an index of     1,and so on.
# 
# 5. Use parantheses: Tuples are typically defined using parentheses,with the elements separated by commas . For example, "(1,2,3,'Neha",4.5)" containing an integer,a string and float.
# 
# 
# So as concerned with the second part of the questions , we can say that tuples are immutable.

# ## Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why tuples have only two in-built methods as compared to Lists.
# 
# The two tuple method in Python are :
# 
# 1. count() : This method returns the number of occurences of a specified value in a tuple.
# 
# example:
# 

# In[10]:


my_tuple= (1,2,3,2,3,4,2,2,2,9)


# In[12]:


count=my_tuple.count(2)
print(count)


# 2. index() : This method returns the index of the first occurrence of a specified value in a tuple.
# 
# example :

# In[ ]:


my_tuple= (1,2,3,2,3,4,2,2,2,9)


# In[13]:


index= my_tuple.index(4)
print(index)


#  Tuples have only two in-built methods as compared to Lists because tuples are immutable,which means their values cannot be changed once they are defined . As a result,there is no need for methods like "append()", "insert()","remove()" and "pop()" that modify the tuple,which is the case for lists. The two methods that are available for tuples are meant to be used for searching and counting elements,rather than modifying them.

#  ## Q3. Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove duplicates from the given list.
# List =
# [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
# 

# #### Ans- In Python,the set datatype does not allow duplicate items. We can use a set to remove duplicates from a given list. Here's the code to remove duplicates from the given list using a set:

# In[6]:


my_list = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
unique_list = set(my_list)
print(list(unique_list))


# ## Q4. Explain the difference between the union() and update() methods for a set. Give an example of each method.
# 

# ### Ans- Both 'union()' and 'update()' are methods in python that are used to combine two or more sets. However,there is a diffference between the two methods.
# 
# ### 'union()' methods returns a new set that contains all the elements from the original set(s) and the set(s) passed as arguments. The original sets remain unchanged. Here is an example of using the 'union()' method:

# In[14]:


set1 = {1,2,3}
set2 = {3,4,5}
set3 = {5,6,7}

new_set = set1.union(set1, set2)
print(new_set)

print(set1)


# ###  On the other hand, 'update()' method modifies the original set by adding all the unique elements from the set(s) passed as arguments . Here's an example of using the 'update()' method : 

# In[15]:


set1 = {1,2,3}
set2 = {3,4,5}
set3 = {5,6,7}

new_set = set1.update(set2,set3)

print(set1)


# ### Conclusion , the 'union()' methods returns a new set with all unique elements from the original and the additional sets, while the 'update()' method modifies the original set by adding unique elements from the additional sets.

# ## Q5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.
# 

# ### Ans- In Python, a dictionary is a data structure that stores data as key-value pairs. Each key in a dictionary maps to a corresponding value . Dictionaries are also sometimes referred  to as associative arays or hash tables.
# 
# ### Here is an example of a dictionary in Python :

# In[ ]:


dict = {"apple":3, "banana":2, "orange": 1}


# ### Dictionaries in Python are unordered, which means that the order in which the key-value pairs are stored is not necesarily the same as the order in which they were added . 

# ## Q6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level nested dictionary.
# 

# ### Ans- Yes we can create a nested dictionary in Python . A nested dictionary is a dictionary that contains other dictionaries as its values . Each key in the outer dictionaray maps to an inner dictionary as its value.
# 
# ### Here's an example of a simple one-level nested dictionary:

# In[9]:


nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}
print(nested_dict)


# ## Q7. Using setdefault() method, create key named topics in the given dictionary and also add the value of the key as this list ['Python', 'Machine Learning', 'Deep Learning']
# 
# ### dict1 = {'language': 'Python', 'course': 'Data Science Masters'}
# 

# ### Ans- To create the key 'topics' and add the list ['Python','Machine Learning','Deep Learning'] as its value in the given dictionary,we can use the 'set default()' metehod. Here's how we can do it:

# In[10]:


dict1 = {'language': 'Python', 'course':'Data Science Masters'}
dict1.setdefault('topics',['Python','Machine Learning','Deep Learning'])


# ## Q8. What are the three view objects in dictionaries? Use the three in-built methods in python to display these three view objects for the given dictionary.
# 
# ### dict1 = {'Sport': 'Cricket', 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

# ### Ans- In Python, dictionaries have three view objects that provide a dynamic view of the dictionary's contents. These view objects are:
# 
# 1. 'dict.keys()': returns a dynamic view objects that contains the keys of the dictionary.
# 2. 'dict.values()': returns a dynamic view object that contains the values of the dictionary .
# 3. 'dict.items()' : returns a dynamic view object that contains the key-value pairs of the dictionary as tuples.
# 
# ###### Here's how you can display these three view objects for the given dictionary 'dict1':

# In[4]:


dict1 = {'Sport': 'Cricket', 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}
print("Keys view object:",dict1.keys())
print("Values view object:",dict1.values())
print("Items view object:",dict1.items())


# #### The view objects returned by these methods are dynamic ,which means they reflect the changes made to the dictionary even after they have been created.

# In[ ]:




