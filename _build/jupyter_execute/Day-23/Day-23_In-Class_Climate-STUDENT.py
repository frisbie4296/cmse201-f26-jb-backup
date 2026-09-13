#!/usr/bin/env python
# coding: utf-8

# # Day 23 In-class Assignment: A simple model for global temperature

# ### <p style="text-align: right;"> &#9989; Put your name here.</p>
# 
# #### <p style="text-align: right;"> &#9989; Put your group member names here.</p>

# <img src="https://i.imgur.com/DyApJbB.png" width=400px>
# 
# ## Goals for today's in-class assignment
# 
# * Use the simple model you implemented in the pre-class assignment, as well as the datasets that you analyzed in the previous class period, to make models that predict global climate change under a variety of circumstances.
# 
# ## Assignment instructions
# 
# Work with your group to complete this assignment. Instructions for submitting this assignment are at the end of the notebook. The assignment is due at the end of class.  If you haven't completed all sections of the assignment, you still need to upload something!
# 
# **In today's class**, we are going to work with the simple climate model you implemented in the pre-class assignment, as well as some of the datasets that you analyzed in the previous class period.  
# 
# ---
# &#9989;&nbsp; **Before we do anything else,** check with the members of your group to make sure that you have correctly implemented the model - in particular, that you get the correct increase in temperature for the assumed carbon input!

# ## Step 1: Verify the model parameter using data
# 
# In the pre-class assignment, we started the model in the year 2000 with a CO$_2$ concentration of 368 parts per million (ppm) and an average global temperature was 15° C (59° F).  We also assumed that the climate sensitivity factor, S, in the model is 3° C.
# 
# &#9989;&nbsp; But now, you're going to calculate temperatures from 1960-present **using only the CO$_2$ concentration data from that time period**. Then you will **plot your calculated temperature values along with the measured values from ```GLB.Ts.csv``` to see how they compare**.
# 
# The CO$_2$ concentration values you'll use to predict the temperature are stored in ```co2_mm_mlo.txt```, so you'll need to **load this dataset as well to use it for calculating your temperature values**.
# 
# You will compare those computed temperatures with the measured values in the ```GLB.Ts.csv``` file.  Remember that this stores temperature anomaly values in $0.01$ K, which you need to convert like you did in our last class period. Also, assume that the average global temperature  was **14.3° C** when the CO$_2$ started in ~1960 (since the data just provides the temperature *difference*, not the absolute temperature, you'll need to add this value to the anomaly data).
# 
# Once you've computed the temperature values using the CO$_2$ data, make your best estimate of the climate sensitivity factor **using the observed temperature data** over the period when you have both temperature and CO$_2$ concentration (approx. 1960 - present). You can do this by overplotting your modeled temperature values with the actual temperatures and changing the sensitivity factor to see how it changes the results.
# 
# **Was our original estimate of S = 3° C a reasonable choice?** What happens when you make this value bigger/smaller?

# In[ ]:


# Put your code here


# <font size="+3">&#9998;</font> *Comment on our choice of value for the sensitivity factor, S.*

# ---
# ## Step 2: Make predictions for the future
# 
# Now, let's go back to our original "very, very simple model" and modify it to make it more sophsticated, and to make some predictions for the future.
# 
# &#9989;&nbsp; Consider the following scenarios, and predict global temperature from the current 2000 until the year 2100. **As you did in the pre-class assignment, start with a CO$_2$ concentration of 368 parts per million (ppm) and an average global temperature of 15° C (59° F).**
# 
# 1.  **Baseline model:** A constant 9 gigatons of carbon per year is put into the atmosphere by humans (this is the model you implemented in your pre-class assignment)
# 2.  **Growth model:** The amount of carbon put into the atmosphere actually grows: starting at 7 gigatons/year in 2000, and increasing by 0.1 gigatons/year for every additional year thereafter (to represent increased reliance on fossil fuels).
# 3.  **"Get it under control" model:** The amount of carbon put into the atmosphere starts at 7 gigatons/year in 2000, increases by 0.1 gigatons/year until 2020, and then decreases by 0.1 gigatons/year until 2100.
# 4.  **"Carbon sequestration" model:** The amount of carbon put into the atmosphere starts at 7 gigatons/year in 2000, increases by 0.1 gigatons/year until 2020, and then decreases by 0.5 gigatons/year until it reaches -5 gigatons/year (indicating that we have developed some means of "sequestering" carbon -- in other words, removing it from the atmosphere.
# 5.  **Your own scenario:** Given your thoughts about climate change and humanity's ability to reduce CO$_2$ emission, devise your own scenario!
# 
# Make plots of the global CO$_2$ concentration, average global temperature, and the rate of human carbon emission each year for each of these scenarios, plotted on the same subplot.  Create a key for the plots so we can tell which lines correspond to which scenario!
# 
# Also, in what scenarios do we avoid increasing global temperatues by no more than 2° C from the current temperature?  Experts consider that to be the global temperature increase that will have [catastrophic climate consequences](http://www.pbs.org/newshour/bb/why-2-degrees-celsius-is-climate-changes-magic-number/), and thus is a critical target for climate models.
# 

# In[ ]:


# Put your code here


# ## Step 3:  How does this impact sea level?
# 
# One major concern with regards to climate change is that global warming will cause a rise in [sea level](https://climate.nasa.gov/vital-signs/sea-level/), which comes from both melting glaciers and ice caps and from the expansion of water as it warms.  This will have significant consequences for ecosystems and also for humans - most of the Earth's population lives close to the ocean, and increased sea level will increase the dangers from flooding and the impact of hurricanes and cyclones, and will displace huge numbers of people in low-lying countries from their homes.
# 
# A recent paper by [Levermann et al. (2013, PNRAS, 110, 13745)](http://www.pik-potsdam.de/~anders/publications/levermann_clark13.pdf) shows calculations that estimate this effect.  Their best prediction is that, over long time scales, **the sea level rise will be approximately 2.3 meters per °C of temperature increase beyond the current value**, although this is substantially uncertain (by roughly a factor of two in either direction).  They also caution that this is the **long-term outcome**, with sea level rise trailing the increase in atmospheric CO$_2$ concentration by some time because it will take some time for the oceans to warm up and the Antarctic ice sheet to melt.
# 
# **Using the Levermann data, make three estimates per model from Step 2:** 
# 
# 1. an "optimistic" model assuming 1 meter of sea level rise per °C of temperature increase beyond the present
# 2. a "realistic" model assuming 2 meters of rise per °C of temperature increase
# 3. a "pessimistic" model assuming 4 meters of rise per °C of temperature increase.  
# 
# Given [this graph of human population distribution by altitude](http://www.radicalcartography.net/index.html?howhigh), how much of the Earth's population might be affected by each of these models?

# In[ ]:


# Put your code here


# ---
# 

# ## Congratulations, you're done!
# 
# Submit this assignment by uploading your notebook to the course Desire2Learn web page.  Go to the "In-Class Assignments" folder, find the appropriate submission link, and upload everything there. Make sure your name is on it!

# # Last In-Class Assignment for this Course--CONGRATULATIONS!!!
# <img src="https://media.giphy.com/media/kyLYXonQYYfwYDIeZl/giphy.gif" width=300>
