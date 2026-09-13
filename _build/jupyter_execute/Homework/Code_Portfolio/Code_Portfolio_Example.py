#!/usr/bin/env python
# coding: utf-8

# # Code Portfolio Example

# # Looping by Index
# ## 1-24-22
# 
# The code below loops by index over the value of `x` and adds 4 to all of the values. 
# 
# When I use this code, I need to change:
# 
# - `range(len(x))` (specifically, the value `x`) to whatever we are looping over.
# - `x[gg] = x[gg]+4` To whatever procedure we want the loop to be repeating.
# 

# In[ ]:


x = [4,12,16,22,33,49]

for gg in range(len(x)):
    x[gg] = x[gg]+4


# # Reading in Data Using Pandas
# ## 1-24-22
# 
# The code below reads in a .csv file using Pandas's `read_csv` function. This should really only be used for CSV files or Excel files (using `read_excel`). Use Numpy's `fromfile` to read in binary (.bin) or Yaff (.yaff) files.
# 
# When I use this code, I need to change:
# 
# - `data` to be a more descriptive variable name.
# - `dataset.csv` to the name of the data file.
# - `delimeter` if the delimeter isn't a comma (other delimeters include `;`).
# - `skiprows` if there are rows at the top of the file I want to skip.
# - `encoding` if the encoding is something other than `utf-8` (other encodings include `utf-16be`).

# In[ ]:


import pandas as pd

data = pd.read_csv("dataset.csv",delimiter=',',skiprows=0,encoding='utf-8')


# # Reading in Data Using Numpy
# ## 1-24-22
# 
# The code below reads in a .bin file using Numpy's `fromfile` function. This works for all kinds of file types, including binary (.bin) and yaff (.yaff). 
# 
# When I use this code, I need to change:
# 
# - `data` to be a more descriptive variable name.
# - `dataset.bin` to the name of the data file.
# - `dtype` to be whatever the data type that this file uses (other commonly used types are `float32`). 

# In[ ]:


import numpy as np

data = np.fromfile('dataset.bin', dtype='int32') 


# # Making a Plot
# ## 1-24-22
# 
# 
# The code below creates a plot showing `x_data` versus `y_data`. 
# 
# When I use this code, I need to change:
# 
# - `x_data` to whatever my `x` variable is.
# - `y_data` to whatever my `y` variable is.
# - `label` to whatever the label fo this dataset is.
# - `xlabel` to whatever the name of my `x` variable is.
# - `ylabel` to whatever the name of my `y` variable is.
# - `title` to whatever the title of this figure should be.

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(x_data,y_data,label="X Data")
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.title("X Vs. Y Dataset")
plt.grid()

