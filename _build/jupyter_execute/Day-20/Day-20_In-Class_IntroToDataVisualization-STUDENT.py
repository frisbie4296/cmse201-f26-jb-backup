#!/usr/bin/env python
# coding: utf-8

# # Day 20 In-Class: Introduction to Data Visualization

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# <img src="https://cdn.thenewstack.io/media/2023/01/285d68dd-charts-1024x581.jpg" width=600>
# 
# ## Learning Goals:
# 
# By the end of this assignment, you should be able to:
# - Compare and evaluate plots

# ## Introduction
# 
# The goal of this assignment is for you and your group to make a compelling plot that is both descriptive and easy to understand. What's more, your plot should **tell a story.** This is meant to be a test run of the skills you'll be expected to demonstrate for the semester project.
# 
# In the pre-class assignment, you were tasked with making a relevant plot for your semester project or based on one of the datasets you found in the Day 12 activities. In today's assignment, you will be:
# 1. Sharing your plot with your group
# 1. Picking (as a group) one plot
# 1. Improving the plot according to the rubric listed in part 3.
# 1. Sharing your plot and competing with your classmates for the best figure.

# ## 1. Sharing out with your group
# 
# #### &#9989;&nbsp; **TASK** As a group, take turns sharing your plots with one another.

# *Use this space to take notes on what your group mates shared**

# ## 2. Picking one plot to work with
# 
# #### &#9989;&nbsp; **TASK** As a group, pick one of the plots to work with. You will be scored using the rubric given in the next section, so it may be worthwhile to read ahead before making your choice.

# ## 3. Create an Effective Plot
# 
# #### &#9989;&nbsp; **TASK** As a group, you will need to make an informative and easy-to-understand plot. Near the end of class, you will present your figure. The presentation will be a competition between the different groups to determine the best plot.
# 
# ### You will be scored by your peers based on the following rubric:
# 1. **Does the plot tell a story? (8 Points)** 
# 1. **No wasted space (3 points)**
# 1. **Labels, legend, and title are informative without cluttering (2 points)**
# 1. **Presenting multi-variable data (2 points)**
# 
# **Total: 15 Points**
# 
# ### 1. Does the plot tell a story? (8 Points) 
# 
# Your plot should be able to stand on its own and inform/convince people of your point. 
# 
# #### **The first ~60-90 seconds of your presentation will be silent; your classmates will look at your plot and try to determine its story.** 
# After this silent part, you will tell the class what point you were trying to get across. Your classmates will then compare your explanation to their interpretation and determine how well your plot told its story.
# 
# ### 2. No wasted space (3 points)
# 
# You only have a finite amount of space on a projector screen, so you want to make sure that every square inch of your plot conveys information. Let's look at an example from Day 13, where we looked at Cocoa exports.
# 
# <img src="https://github.com/msu-cmse-courses/cmse201-S22-data/blob/main/Day-13_NEW/Linear_Plot_Cocoa_Beans_Export.jpg?raw=true" width=800px>
# 
# 
# 
# The problem that we run into here is a considerable amount of wasted space. Most countries export a substantially smaller amount than the countries along the west coast of Africa. Our plot is massive, but we're getting information from ~20%, which is bad. 
# 
# 
# One possible way of dealing with this issue is to change the y-scale to log, which allows you to see information about all of the other countries. 
# 
# <img src="https://github.com/msu-cmse-courses/cmse201-S22-data/blob/main/Day-13_NEW/Log_Plot_Cocoa_Beans_Export.jpg?raw=true" width=800px>
# 
# The trade-off is that unless you know that your audience might not be as comfortable with reading/interpreting log plots, it's functionally useless if no one can understand your plot. You will need to decide what works best for your plot.
# 
# 
# 
# ### 3. Labels, legend, and title are informative without cluttering (2 points)
# 
# The x/y labels, legend, and title are the tools you will use to give your audience context, making them crucial for a well-made plot. 
# 
# Let's again look at the Cocoa bean export plot from above. Our title is a good descriptive summary that isn't taking up too much space. We run into trouble when we try to add too much description, and we end up taking up a lot of space, potentially in attempting to be a little too on the nose with the story of our plot. 
# 
# <img src="https://github.com/msu-cmse-courses/cmse201-S22-data/blob/main/Day-20/Cluttered_Plot_Cocoa_Beans_Export.jpg?raw=true" width=800px>
# 
# Aside from being aesthetically displeasing, too much space is being taken up by text. You want your text to balance giving enough information without becoming the center of attention. We want the eyes to be drawn to the plot first and then look at the text to get context; in this case, it's not clear where we should focus our eyes. Also, **we could probably make some improvements to how we've formatted the axis labels for the x-axis**, right now it's pretty hard to read those. **How might we improve the readability while also perhaps using the space more effectively?**
# 
# 
# ### 4. Presenting multi-variable data (2 points)
# 
# **NOTE: You do not need to have multi-variable data. There is just more points possible for this kind of plot**
# 
# It will often be the case that you'll be dealing with data with multiple dimensions that could be important. In this case, it's important to find a way to include all of the different variables in your plot so that the reader can see all factors in play.
# 
# Let's take a look at the figure from the pre-class assignment. 
# 
# 
# 
# 
# <p align="center">
#     <img src="https://github.com/msu-cmse-courses/cmse201-S22-data/blob/main/Day-20/USA_Gas_Guzzlers.jpg?raw=true" width=500px>
# </p>
# 
# In this figure, we're currently displaying four variables: MPG, Horsepower, Country of Origin, and Weight. This is an excellent example of a plot that has little to no wasted space, has informative text that isn't drawing attention away from the figure, and shows all relevant variables. The figure above is the kind of plot you should be aiming for. 
# 
# 
# 

# ## 4. Present your plot to the rest of the class
# 
# #### &#9989;&nbsp; **TASK** As a group, you will present your plot to the rest of class. Your instructor should have shared a Google Slides or OneDrive Powerpoint presentation with you. When you aren't presenting you will score your classmates plots using [**this score sheet.**](https://forms.office.com/r/HrWVwGLwSw) Please fill out one for each group. 

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
# Submit this assignment by uploading your notebook to the course Desire2Learn web page.  Go to the "In-Class Assignments" folder, find the appropriate submission link, and upload it there. Make sure your name is on it.
# 
# See you next class!

# &#169; Copyright 2023,  Department of Computational Mathematics, Science and Engineering at Michigan State University
