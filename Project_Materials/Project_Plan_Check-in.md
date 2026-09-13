# First Project Checkpoint

The purpose of this assignment is to make sure that everyone is on track to finish their project on time and can articulate their plan. To that end, you will need to submit a short document or notebook that specifies three critical components of your project: 

1. Your research question 
2. The context of your data set and/or any context, assumptions, or potential bias in your algorithm/model
3. The resources that you will use to answer your research question


## 1. Research Question 

When defining a research question for this project, it is recommended that **you look for something you are somewhat comfortable with.** If you are in your third or fourth year and you've taken several major-specific courses, then you could do something related to your major. Otherwise, you may want to draw from the topics we've covered in class. 

### Example research questions
1. How much will sea levels change in the Indian Ocean over the next 100 years?
2. What is the basic reproduction number ($R$) of Covid-19, extrapolated from infections in Michigan?
3. How does the gravitational interaction between a star and a planet cause the star to “Wobble” and how do astronomers use this to detect Exoplanets?

## 2. Data and Algorithm Contexting

As we have explored so far this semester, the context of your data and/or model is critical for conducting ethical work and informing what claims you can make based on your results. To that end, you will be required to articulate the context of your data or model as part of this checkpoint and in your final notebook and presentation. This checkpoint is your chance to ground your work in the context and practice articulating the context. Below, you will see example questions for a Data-intensive project or a Modeling-intensive project. Depending on your choice, you should make sure that you answer the listed questions in your context statement. Your statement can have more content than this but not less. If you aren't sure of the answers to the questions, come to office hours and/or speak with your section instructors!

### What to cover in a Data Context Statement
1. Who collected/generated the data?
2. How was the data collected/generated?
3. Who/what is included in the data?
4. Who/what is **not** included in the data?
5. What are the limitations or biases of the data?
6. Based on the questions you've had to reflect on above, what are you going to do in your project because of this?

### What to cover in an Algorithm or Modeling Context Statement
1. What model are you going to use (e.g. mathematical model, curve fitting, differential equations, compartmental model, Agent-based model, etc.)
2. What assumptions will go into your model?
3. What biases might be present in your model?
4. What are the limitations of your model?
5. How might your assumptions and biases affect your claims?
6. Based on the questions you've had to reflect on above, what are you going to do in your project because of this?

## 3. Resources You Will Use

To answer your research question, you will need to use one or more outside resources. 

If your project incorporates data analysis, you should **link to the specific datasets you will be using and provide an example dataset.**

- For example, if I were going to model temperature variations in East Lansing, I would include a link to the [NOAA website](https://www.ncdc.noaa.gov/cdo-web/datatools/lcd) I used to find my data and an example dataset (included in this assignment).


If your project incorporates computational modeling, you should **link to, or provide a copy of, the website/paper/book/etc. that explains the model you’ll use.**
- For example, if I was going to model epidemics using something like the SIR model we talked about in class, but I wanted to include underlying population growth, I might use resources like [this paper on epidemiological modeling](https://www.alessandro-giua.it/UNICA/ACCPS/material/Hethcote_2000.pdf).

# Example Submission (Data Intensive)

## Research Question 

#### “What behavioral patterns do squirrels in Central Park have?”

## Context
The Central Park Squirrel dataset was collected by the Squirrel Census. The Squirrel Census is a multimedia science, design, art, and storytelling project that counts squirrels in urban green spaces in the US and releases the data to the public. The specific dataset I use in my project comes from Central Park, a large city park located in New York City. The data was collected by the Squirrel Census with the help of hundreds of volunteers and the Explorers Club, NYU Department of Environmental Studies, Macaulay Honors College, the Central Park Conservancy, and New York City Department of Parks & Recreation in October 2018. I found the data on the NYC Open Data Hub, where it has been publicly available since 2019. Each entry in the dataset is a squirrel observation, and contains lots of information about the squirrel’s appearance, behavior, and location in the park.

One thing I noticed is that the data is made up of 3023 raw squirrel observations. We don’t know how many squirrels that live in Central Park were missed, or observed and counted more than once. This project will in part study the distribution of squirrel fur color in Central Park. Given my data, I am making an assumption that squirrels with each distinct fur color are equally likely to be missed and/or overcounted across the park. Therefore, while the numbers of squirrels counts may be inaccurate, the relative proportion of squirrels having each fur color should be reasonable estimates that I will present in my Results section. In addition, I plotted the squirrel data based on location. I found that there were no squirrels in the park’s bodies of water. I learned that squirrels can swim, so it may be possible that swimming squirrels were not counted. 

References:
- https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
- https://www.thesquirrelcensus.com/about
- https://www.skedaddlewildlife.com/location/okanagan/blog/okanagan-can-squirrels-swim/ 

## Resources 
- I will use the data from the Central Park Squirrel Census: https://www.dropbox.com/scl/fi/is2yaa5gz1of32xo1xwvd/squirrel-data.csv?rlkey=sao5wj2tqd98nzs6rsi5k7ot6&e=1&dl=0


# Example Submission (Modeling)

## Research Question 

#### “How is the transmission of disease affected by birth rates?”

## Context
I plan to begin with the basic SIR model we used in class, but I will add birth rate to the relavant compartments/equations. I will maintain the assumptions we had for the model in class, but rather than having a fixed total population, I will assume that the total population can change. Because the SIR model only includes susceptible, infectious, and recovered individuals, there is no way to account for acquired immunity or death. It also assumes that the population is uniformly susceptible - meaning that individual variations in susceptibility (genetics, age, weight, activity, etc.) are not captured. I suspect that this will affect my results because the total population will increase over time because no one is dying. I may make adjustments to the birth rate and try to consider death rate to explore more nuance in the model. I could also deepen my analysis by having age compartments with different susceptibilities. I'm not sure what will happen when I do that, but I plan to make one change at a time and compare the results to known diseases to give me an understanding of how well my model is working.

## Resources 
- I will start with the basic code from in class and the paper provided with adaptations of the model as a guide for where to start

# What you will Submit

### - A single document, either a PDF or a ipynb notebook.
### - The document must contain:
#### 1. Your name
#### 2. Your section
#### 3. Your research question
#### 4. Your context statement draft
#### 5. Links to any resources you will use and a brief description of how you will use them.
### - If you plan on using data, you must also submit *the specific dataset* that you will be using. It should be either a CSV or Excel (.xlsx) file. 

