#!/usr/bin/env python
# coding: utf-8

# # Day 22 Pre-class:  Global warming and climate modeling

# ## <p style="text-align: right;"> &#9989; Put your name here</p>

# ## Goals for today's pre-class assignment
# 
# * Read about the greenhouse effect and the ways that global temperature and carbon dioxide levels are calculated
# * Make plots to explore the relationship between global temperature and sea level over the past three million years
# 
# ## Assignment instructions
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-class assignments" submission folder on D2L.  If you run into issues with your code, make sure to use Slack to help each other out and receive some assistance from the instructors. Submission instructions can be found at the end of the notebook.

# ---
# ## Understanding the Earth's climate
# 
# Over the next two assignments, you will be using a combination of data analysis and modeling to understand the Earth's climate and the relationship between greenhouse gases and temperature in the Earth's atmosphere.  We'll use many of the techniques that you have learned this semester to do so!
# 
# Global climate change is a huge and complex issue, with important consequences for [global peace and human development](https://blog.oup.com/2017/06/climate-change-global-peace-security/), particularly in countries that are not particularly wealthy or technologically advanced (and thus will have greater challenges dealing with a changing world).
# 
# **In preparation for the in-class assignment,** you need to read and think about how global temperatures are measured, and examine historical climate and sea level data.
# 
# ---
# 
# &#9989;&nbsp; First, **read** the Wikipedia articles on [the global temperature record](https://en.wikipedia.org/wiki/Global_temperature_record), [paleoclimatology](https://en.wikipedia.org/wiki/Paleoclimatology) (that is, the study of climate changes over the entire history of the Earth), and [this NASA article on estimating historical temperatures](https://www.giss.nasa.gov/research/briefs/1999_schmidt_01/).
# 
# In the box below, **describe how we estimate the Earth's  atmospheric temperature in the last few hundred, tens of thousands, and millions of years.  How confident are scientists in these predictions?**

# <font size="+3">&#9998;</font> *Put your answers here!*

# ---
# 
# The file ```bintanja2008.txt``` is included with this assignment, and is from the journal article "North American ice-sheet dynamics and the onset of 100,000-year glacial cycles," by Bintanja and van de Wald ([2008, Nature, **454**, 869-872](https://www.nature.com/articles/nature07158)).  The dataset that comes from [this archive](https://www.ncdc.noaa.gov/paleo-search/study/11933) at the [National Centers for Environmental Information](https://www.ncdc.noaa.gov/), and is a reconstruction of the global surface temperature, deep-sea temperature, ice volume, and relative sea level for the last **3 million years**.  Note that this file has been very slightly modified to remove some characters that Numpy and Pandas have problems with (letters with accents), but actual data has not been changed!
# 
# Before you make any plots, open up the file and look at the header.  In particular, look at the description of the various columns of data!  Note that column 9, "Global sea level relative to present," is in confusing units - more positive values actually correspond to *lower* sea levels than less positive values. Also "BP" means "Before Present." 
# 
# Now, let's load up the data and make some plots!
# 
# &#9989;&nbsp; **First**, read in the data file using Numpy's [loadtxt()](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) method and put the various columns into Numpy arrays.  It's fine to load all of the data into a single combined multi-dimensional array if you want, or split the data into multiple arrays. 
# 
# **HINTS:**  The header is 109 rows long, and the file is set up so that each column is a separate dataset (so you may wish to remind yourself of how the ```unpack``` argument for ```loadtxt``` works)

# In[ ]:


# Put your code in this cell!


# &#9989;&nbsp; Now, make a [subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html) that has four panels, which show:
# 
# 1. The atmospheric surface temperature as a function of time (column 5 in the dataset)
# 2. The deep sea temperature as a function of time (column 6 in the dataset)
# 3. The depth of ice covering North America as a function of time (column 8 in the dataset)
# 4. The global sea level relative to the present (column 9 in the dataset)
# 
# **Plot the relationships for all three million years of the dataset.**  Please note that column 9, "Global sea level relative to present," is in confusing units - more positive values actually correspond to *lower* sea levels than less positive values.  You may want to multiply column 9 by -1 in order to get more sensible values.  Also, [modify the x-axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html) of each subplot so that it goes from (3000,0) instead of (0,3000), so that time moves forward from left to right! (Note that the time is reported in kiloyears; 1 kyr = 1000 yr; 1 million years = 1000 kyr). You can do this using the `plt.xlim()` function!

# In[ ]:


# Put your code in this cell!


# &#9989;&nbsp; Now, make a copy of the previous plot that **zooms in on the last 500,000 years of the dataset.** We'll use this to examine some trends. You can do this by changing the values you feed to the `plt.xlim()` function.

# In[ ]:


# Put your code in this cell!


# &#9989;&nbsp; **Based on the plot you've made, answer the following questions:**
# 
# 1.  What relationship do you see between the global atmospheric temperature and the deep sea temperature?
# 2.  What relationship do you see between the global atmospheric temperature and the estimated volume of ice on land?
# 3.  What relationship do you see between the volume of ice and the estimated sea level?
# 4.  Do the relationships that you're seeing make sense to you?  Why or why not?
# 5.  Do you see patterns that repeat in time?  And if so, on what timescales do they seem to occur?

# <font size="+3">&#9998;</font> *Put your answers here!*

# ---
# ## Assignment wrap-up
# 
# Please fill out the form that appears when you run the code below.  **You must completely fill this out in order to receive credit for the assignment!**

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://cmse.msu.edu/cmse201-pc-survey" 
	width="800px" 
	height="600px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Pre-class assignments" folder, find the appropriate submission link, and upload it there.
# 
# See you in class!

# &#169; Copyright 2018,  Michigan State University Board of Trustees
