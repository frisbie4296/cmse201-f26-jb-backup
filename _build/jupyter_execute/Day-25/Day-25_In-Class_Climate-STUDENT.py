#!/usr/bin/env python
# coding: utf-8

# # Day 25 In-class Assignment: Analyzing climate data

# ### <p style="text-align: right;"> &#9989; Put your name here.</p>
# 
# #### <p style="text-align: right;"> &#9989; Put your group member names here.</p>

# <img src="https://imagecache.jpl.nasa.gov/images/edu/activities/temp_graphing_main-640x350.jpg" width=500px>
# 
# ## Goals for today's in-class assignment
# 
# * Analyze multiple datasets to understand trends and correlations between different experimental measurements relating to the Earth's climate
# 
# ## Assignment instructions
# 
# Work with your group to complete this assignment. Instructions for submitting this assignment are at the end of the notebook. The assignment is due at the end of class.  If you haven't completed all sections of the assignment, you still need to upload something!

# ---
# **In today's class**, we are going to examine several datasets that show how various quantities (such as global temperature and atmospheric carbon dioxide levels) have evolved over time.  The datasets that we will use are:
# 
# ### Direct measurments from modern era:
# 1. `GLB.Ts.csv`: Measurements of global mean air temperatures from 1880 through the present day. Note that temperatures are in hundredths of a degree Kelvin. The header is 1 line long.
# 
# 2. `co2_mm_mlo.txt`: Measurements of average monthly atmospheric carbon dioxide (CO2) concentration from 1958 through the present. The header is 72 lines long.
# 
# 3. `ch4_annmean_gl.txt`: Measurements of average average yearly methane (CH4) concentrations from 1984 through the present. The header is 56 lines long.
# 
# ### Estimates from marine sediment data:
# 
# 4. `bintanja2008.txt` -- A reconstruction of the global surface
# temperature, deep-sea temperature, ice volume, and relative sea level
# for the last 3 million years.  The header is 109 lines long.
# 
# ### Estimates from ice core data: 
# 
# 5. `vostok-deutnat.txt`: Reconstructions of the global atmospheric
# temperature using ice core data.  Note that column 2 is ice age (i.e.,
# number of years in the past) and column 4 is the temperature
# difference from the present day in degrees Kelvin.  The header is 111
# lines long.
# 
# 6. `vostok-co2nat.txt`: Reconstructions of the global carbon dioxide
# (CO2) concentration using ice core data.  The header is 155 lines
# long.
# 
# 6. `vostok-ch4nat.txt`: Reconstructions of the global methane (CH4)
# concentration using ice core data.  The header is 86 lines long. 
# 
# Open up each of the datasets and look at the headers - that is, the block of text at the top that describes what's in the file.  You will have to do this to understand which columns you want to use, what the units are, and so on.  Additional details on these data files are provided at the bottom of this notebook.
# 
# ---
# 
# ### &#9989;&nbsp; Using Numpy, read each of these datasets into numpy arrays!
# 
# You may run into confusing issues if you try to use Pandas to read in these datasets. Given this, you are expected to use `np.loadtxt()` to read them in. You will have to take into account the fact that each of the files has a header of a different length - you can either figure the length out yourself, or **look at the README provided at the bottom of this notebook**.  You also need to **modify the times and temperatures for each dataset so that they have consistent units** (since some datasets are in "years before present", whereas others use the Gregorian dating system, and some of the datasets use temperature differences in Kelvin whereas others use hundredths of a Kelvin. If you're not familiar with Kelvin as a temperature unit, look [here](https://en.wikipedia.org/wiki/Kelvin)).
# 
# **The comments provided for you in the cell below explain how you need to modify the datasets to make them consistent and which columns are important.**

# In[ ]:


# put your code here

# load in GLB.Ts.csv
# You want columns 0 and 13, which are time in Gregorian time and temperature in 0.01 K
# You should divide the temperature anomaly values by 100 to get them in Kelvin
global_temp_recent = np.loadtxt('GLB.Ts.csv',skiprows=1,unpack=True,delimiter=',')
global_temp_recent[13] /= 100.0


# load in co2_mm_mlo.txt
# column 2 is year with decimal dates, column 4 is CO2 in PPM (interpolated to fill missing values)
# There's nothing you need to change for this dataset



# load in ch4_annmean_gl.txt
# column 0 is year, column 1 is CH4 in PPB
# There's nothing you need to change of this dataset

# load in bintanja2008.txt
# column 0 is time in kiloyears before 2018, and column 4 is atmospheric temperature
# You should multiply the time values by -1000 and add 2018 to get them in the right units
global_temp_bintanjan = np.loadtxt('bintanja2008.txt',skiprows=109,unpack=True)

global_temp_bintanjan[0] *= -1000.0
global_temp_bintanjan[0] += 2018.0


# load in vostok-deutnat.txt
# column 1 is the ice age (in years before 2001), column 3 is delta-T in K
# You should mutiply the time information by -1 and add 2001 to get them in the right units
vostok_temp = np.loadtxt("vostok-deutnat.txt",skiprows=111,unpack=True)
vostok_temp[1] *= -1.0
vostok_temp[1] += 2001.0


# load in vostok-co2nat.txt
# column 0 is the ice age (in years before 2001), column 1 is concentration in ppm
# You should mutiply the time information by -1 and add 2001 to get them in the right units
vostok_co2 = np.loadtxt("vostok-co2nat.txt",skiprows=155,unpack=True)
vostok_co2[0] *= -1.0
vostok_co2[0] += 2001.0


# load in vostok-ch4nat.txt
# column 0 is the ice age (in years before 2001), column 1 is concentration in ppb
# You should mutiply the time information by -1 and add 2001 to get them in the right units



# ---
# ### Now, let's examine the datasets!
# 
# You've already looked at the Bintanjan dataset in the pre-class assignment, so we won't worry about that for the time being.
# 
# &#9989;&nbsp; But, let's make a matplotlib subplot that shows the global temperature, CO2, and CH4 concentrations since 1880 (and in the case of the CO2 and CH4 data, for as long as you have data) using the files ```GLB.Ts.csv```, ```co2_mm_mlo.txt```, and ```ch4_annmean_gl.txt```.  Make sure that they all have the same x-axis! You should get something that looks like this:
# 
# <img src="https://i.imgur.com/MmbnL1l.png">

# In[ ]:


# put your code here


# &#9989;&nbsp; **Question:** What relationship do you see between the temperature, CO2 concentration, and CH4 concentration in the recent data?

# <font size="+3">&#9998;</font> *Put your answers here!*

# **Now, let's visualize the Vostok ice core data.**
# 
# &#9989;&nbsp; Make a subplot that shows the same three quantities - temperature, CO2 concentration, and CH4 concentration - as a function of time.
# 
# Your plot should end up looking similar to this:
# 
# <img src="https://i.imgur.com/aIgnsun.png">

# In[ ]:


# put your code here


# &#9989;&nbsp; **Questions:** 
# 
# 1.  Does this data suggest similar relationships between the temperature, CO2, and CH4 concentrations as the data you examined above?
# 2.  Does this data show the same patterns as the Bintanjan data that you displayed as part of your pre-class assignment?
# 

# <font size="+3">&#9998;</font> *Put your answers here!*

# **Now, let's put both on the same plot.**
# 
# &#9989;&nbsp; To put the ice core measurements in context, adjust the *subplot above* so that it shows the most recent temperature, CO2 and CH4 measurements *from the dataset that spans from 1880-2020.*  This can be done using either a red circle or a horizontal line. 

# &#9989;&nbsp; **Questions:** 
# 
# 1.  How does the most recent temperature measurement compare with the range in the ice core measurements?
# 2.  How do the most recent CO2 and CH4 concentrations compare?

# ---
# ### Now, let's make some predictions
# 
# Now, let's extrapolate this data into the future - in particular, we want to predict how global carbon dioxide concentration, and also global temperature, will rise over the next few decades if current trends continue.
# 
# &#9989;&nbsp; Examine how both global temperature and global CO2 concentration have changed since 1960.  Do the trends look like linear trends, exponential trends, or something else?  Choose a reasonable period of time over which to fit the data (at least several decades), and fit the appropriate curve to the data.  Answer this question: *What will the global temperature and CO2 concentrations be 20, 50, and 100 years from now?*
# 
# **Show this with a plot, and describe your outcomes below**.  (Hint: try using SciPy's [curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) methods!)
# 
# If you decide it would be useful, one possible general equation for an exponential curve is:
# 
# $$ f(t) = A e^{B(t-C)} + D $$
# 
# If you're going to use the exponential function, you will need to use `p0` keyword to make an initial guess (and the initial guess will need to be pretty good!).

# In[3]:


# put your code here


# <font size="+3">&#9998;</font> *Describe your findings here!*

# ---
# # Datasets README
# 
# 
# 1. Measurements of global mean air temperatures from 1880 through 2015. Specifically, these are recorded as **deviations from the mean temperature** at a particular time. This data, in the file ```GLB.Ts.csv```, comes from the [NASA GISS surface temperature website](http://data.giss.nasa.gov/gistemp/), "Global-mean monthly, seasonal, and annual means, 1880-present."  See [this file](http://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts.txt) for clues as to what the columns mean.  Note that these temperatures are measured directly (i.e., with thermometers), rather than estimated using a proxy!
# 2. Measurements of average monthly atmospheric [carbon dioxide](https://en.wikipedia.org/wiki/Carbon_dioxide) (CO2) concentration from 1958 through the present, measured at the Mauna Loa Observatory in Hawaii.  This data, in the file ```co2_mm_mlo.txt,``` comes from the [Earth Systems Research Laboratory](https://www.esrl.noaa.gov/gmd/ccgg/trends/) global monitoring division, and can be [found here](ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt).  Note that the "concentration" data is reported in units of "micromol/mol", meaning parts per million in the atmosphere.  This data is measured directly.
# 3. Measurements of average average yearly [methane](https://en.wikipedia.org/wiki/Methane) (CH4) concentrations from 1984 through the present, measured at a variety of locations around the world.  This data, in the file ```ch4_annmean_gl.txt```, also comes from the [Earth Systems Research Laboratory](https://www.esrl.noaa.gov/gmd/ccgg/trends_ch4/), and can be [found here](ftp://aftp.cmdl.noaa.gov/products/trends/ch4/ch4_annmean_gl.txt).  In this file, the "concentration level" is listed in parts per billion (rather than parts per million, as was done with CO2).  This data is measured directly.
# 
# 4. A reconstruction of the global surface temperature, deep-sea temperature, ice volume, and relative sea level for the last **3 million years**.  This data, in the file ```bintanja2008.txt```, comes from the National Oceanic and Atmospheric Administration's National Climatic Data Center website, and can be [found here](https://www.ncdc.noaa.gov/paleo-search/study/11933).  Note that the temperature measurements in this file are estimated using a proxy measurement using the chemical composition of core samples from ocean sediments.
# 
# 5. Reconstructions of the global atmospheric temperature, as well as atmospheric CO2 and CH4 levels, from [ice core samples](https://en.wikipedia.org/wiki/Ice_core) taken at the [Vostok Research Station](https://en.wikipedia.org/wiki/Vostok_Station) in Antarctica.  Again, the temperature values are recorded as deviations from the mean temperature at a particular time. This data is in the files ```vostok-deutnat.txt``` (temperature), ```vostok-co2nat.txt``` (CO2), and ```vostok-ch4nat.txt``` (CH4).  This data was obtained from the [National Centers for Environmental Information](https://www.ncdc.noaa.gov/) and can be found [at this web page](https://www1.ncdc.noaa.gov/pub/data/paleo/icecore/antarctica/vostok/).  The temperature is estimated; CO2 and CH4 concentrations are measured directly from the ice.

# ---
# ## Assignment wrapup
# 
# Please fill out the form that appears when you run the code below. **You must completely fill this out in order to receive credit for the assignment!** 

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://cmse.msu.edu/cmse201-ic-survey" 
	width="800px" 
	height="600px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ## Congratulations, you're done!
# 
# Submit this assignment by uploading your notebook to the course Desire2Learn web page.  Go to the "In-Class Assignments" folder, find the appropriate submission link, and upload everything there. Make sure your name is on it!

# &#169; Copyright 2023,  Michigan State University Board of Trustees
