#!/usr/bin/env python
# coding: utf-8

# # Day 18 In-class Assignment: Building Compartmental Models
# 

# ### <p style="text-align: right;"> &#9989; Put your name here.</p>
# 
# #### <p style="text-align: right;"> &#9989; Put your group member names here.</p>

# ### Goals for today's assignment:
# 
# * Think about how to build compartmental models for a variety of applications.
# 
# 
# ### Assignment instructions:
# 
# In today's class you will be building three compartmental models. **There will be no coding today**, although you will code models like these later in the week. The goal today is learning to construct models. 
# 
# To ensure you are able to complete all three, be sure to budget your time accordingly. One idea is to take the amount of time you have left as of right now, divide by three and set a timer. (For example, you can type `timer 15 minutes` into Google and it will start a timer for you.) The instructor will also help to keep you on time.
# 
# You might start with:
# * 15 minutes to brainstorm with your group, drawing a variety of variants of possible models. 
# * 10 minutes to write the answers to the questions below. (You will likely improve your model as you write this.)
# * 5 minutes to transition to the next model. 
# 
# **Read below to learn what you're expected to turn in for this assignment.**

# ___
# ## What you need to turn in at the end of class.
# ___
# * The names of the people in your group.
# * A picture of each of the three compartmental models. **You can draw these on your whiteboard or some sort of virtual whiteboard. You will need to save a picture of it.** You can choose the platform that works best for your group!
#    - Think about which compartments you will need: what are the interacting things your model needs?
#    - Think about how these things interact, and draw a diagram like this to show those connections. 
#    
# <div align="center"><img src="http://www.pmod.com/files/download/v31/doc/pkin/2389.png" width=500px></div>
# 
#    - Think about whether the connections are arrows or just lines, do the arrows go in both directions? Think about what is causing the influence of one compartment on another and at what rate that might be happening.
#    - Be creative: use different colors, sizes, line types (e.g., dashed): the goal is to be able to express your model in a form that you can discuss it logically and be able to ultimately use it as a guide for coding it (perhaps using ODEs).
# 
# 
# &#9989;&nbsp; **You will also need to write written description of each of the model**:
# *  What are the compartments you chose? Why did you choose those? Which did you consider that you felt were not needed? 
# *  What are the dependencies between the compartments? Are there transitions between all of the compartments? Or, do some of the compartments only influence the other compartments? 
# * How many parameters does your model have? How would you go about getting these parameters?
# * Once this model is complete and coded, how would you test it? What could you use the model for?
#     
# Note that this project is fairly opened ended. This is because _reality_ is open ended. You will be assessed on your ability to work as a team to come up with a logical and credible model, not to find the "correct" answer (which likely doesn't exist anyway).
# 
# One of the most important issues we face when building models is what needs to go into the model and what doesn't. Use whatever web resources you need to gather information and data; none of us are experts on the topics below, and a little research can help you build something credible.

# ---
# ___
# # Health: Infectious Disease Pandemic
# ___
# 
# We'll take a moment to watch the following video as a class.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('1QLgXzyXOH0',width=640,height=360,start=0,end=225)


# Infectious diseases have killed millions of people in the past century.
# 
# <img src="https://s-media-cache-ak0.pinimg.com/originals/92/52/d1/9252d1487c065b2f18e8c4c28f19198c.jpg" width=500px>
# 
# One class of diseases includes respiratory viral diseases, like the common cold, measles and influenza. 
# 
# Design a compartmental model that describes a population of people in which a new virus is introduced. Imagine that the virus is spread through the human population through only human-to-human interactions (for example, a cold, flu, HIV, but in contrast to the Zika virus, which is spread by infected mosquitos).
# 
# Some things to consider:
# * Which human diseases do you get over and which ones do you keep for life?
# * Which diseases do humans get from other animals? How would you model that in comparison to a disease that is only transferred between humans?
# * How can your models include prevention, use of vaccines/drugs, or [social distancing](https://en.wikipedia.org/wiki/Social_distancing)?
# * How would models for these disease differ: HIV, cold, ebola, HPV? 
# 
# 
# Use the markdown cell below to describe the compartmental models that you built and remember to upload a photo of your compartmental model.

# **Our models...**

# ___
# # Ecology: Sharks versus Cape Fur Seals
# ___
# 
# Before moving to the next model, we'll take a moment to watch the following video as a class. For more information, check out this work from [Miami University!](https://news.miami.edu/rosenstiel/stories/2019/02/new-study-finds-ecosystem-changes-following-loss-of-great-white-sharks.html)

# In[2]:


from IPython.display import HTML
HTML('<iframe src="https://player.vimeo.com/video/309578154?h=c38bf8192b" width="640" height="360" frameborder="0" allowfullscreen></iframe><p>')


# In the waters around South Africa there are many seals. They swim around, they eat fish, they have children (pups); left unchecked, they’re population would just keep growing until they ran out of food. But these seals are themselves food for the deadly great white sharks.
# 
# <img src="https://images.fineartamerica.com/images-medium-large/harbor-seals-sunbathing-on-the-beach-40d7553-wingsdomain-art-and-photography.jpg" width=500>
# 
# 
# Design a compartmental model that describes this situation following the instructions given above. 
# 
# Some things to consider:
# - Do you think that all seals are eventually eaten by sharks?
# - What might happen to the seals if the fish that they eat were all killed/eaten?
# 
# Use the markdown cell below to describe the compartmental models that you built and remember to upload a photo of your compartmental model.

# **Our models....**

# ___
# # Social Science: Spread of Rumors
# ___
# 
# Before starting the final model, we'll take a moment to watch the following video as a class.

# In[3]:


from IPython.display import YouTubeVideo
YouTubeVideo('oSNj3tHnLWM',width=640,height=360)


# Rumors have been with us as long as we have been here.
# 
# <img src="https://images.techhive.com/images/article/2016/08/rumors-100677553-large.jpg" width=500>
# 
# It has not always been well understood how rumors start, how long they last and why they seem to die away. This particular problem is connected to how jokes spread, how propaganda can be used against a society and how people develop their culture. 
# 
# Design a compartmental model that describes how a rumor spreads through society. 
# 
# Things to think about:
# - If someone hears a rumor ten times in one day, do you think they’re more or less likely to spread it?
# - If someone hears a rumor about their friend that they know isn’t true, are they likely to spread it?
# - Think about recent events in the news that involve influencing presidental elections using social media. How would you model this?
# 
# 
# Use the markdown cell below to describe the compartmental models that you built and remember to upload a photo of your compartmental model.

# **Our models...**

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


# ### Congratulations, you're done!
# 
# Submit this assignment by uploading your notebook and the pictures of your models it to the course Desire2Learn web page.  Go to the "In-Class Assignments" folder, find the appropriate submission link, and upload everything there. Make sure your name is on it!

# &#169; Copyright 2023,  The Department of Computational Mathematics, Science and Engineering at Michigan State University
