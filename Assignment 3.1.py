
# coding: utf-8

# # Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[16]:


# Creating an object to compute 5/0 in return
def compute():
    return 5/0


# In[20]:


# catching the exception as a Zero Division Error using 'try' block
try:
    compute()
except ZeroDivisionError:
    print('Gonna divide it by a zero?')

# Using a finally block to just execute
finally:
    print('It will just give you an infinity!')

