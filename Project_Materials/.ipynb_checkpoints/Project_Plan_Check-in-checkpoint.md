# Project Checkpoint
## Due at 11:59pm on **Nov 6** for M/W sections and **Nov 7** for T/Th sections
<br>

## Assignment goals:
The purpose of this assignment is to make sure that everyone is on track to finish their project on time. To that end, you will need to submit a short document or notebook that specifies two critical components of your project: 

1. Your research question 
2. The resources that you will use to answer your research question

### 1. Picking a research question 

When defining a research question for this project, it is recommended that **you look for something you are somewhat comfortable with or have some prior familiarity with**. If you are in your third or fourth year and you've taken several major-specific courses, then you could do something related to your major. Otherwise, you may want to draw from the topics we've covered in class or topics related to hobbies or passions you might have. Ulimately, we want you to pick a topic you're excited about, so you can stray beyond these recommendations, but be aware that if you're not familiar with the topic, you may need to invest additional time in understanding some of the nuance of that topic. 

#### Example research questions
1. How much will sea levels change in the Indian Ocean over the next 100 years?
2. What is the basic reproduction number ($R$) of Covid-19, extrapolated from infections in Michigan?
3. How does the gravitational interaction between a star and a planet cause the star to “Wobble” and how do astronomers use this to detect Exoplanets?

### 2. Identifying the resources you will use

To answer your research question, you will need to use one or more outside resources. 

If your project incorporates data analysis, you should **link to the specific datasets you will be using and provide an example dataset.**

- For example, if I were going to model temperature variations in East Lansing, I would include a link to the [NOAA website](https://www.ncdc.noaa.gov/cdo-web/datatools/lcd) I used to find my data and an include an example dataset in my submission.

If your project incorporates computational modeling, you should **link to, or provide a copy of, the website/paper/book/etc. that explains the model you’ll use.**
- For example, if I was going to model epidemics using something like the SIR model we talked about in class, but I wanted to include underlying population growth, I might use resources like [this paper on epidemiological modeling](https://www.alessandro-giua.it/UNICA/ACCPS/material/Hethcote_2000.pdf).

---
# What you will Submit

**A single document, either as a PDF or a Jupyter (.ipynb) notebook.** (Documents from a word processor, like Microsoft Word, will not be accepted. Of course, you could certainly use something like MS Word to make your PDF)

The document **must contain**:
1. Your name
2. Your section number
3. Your current research question
4. Links to any resources you will use and a brief description of how you will use them.
    * If you plan on using data for your project, you must also submit *the specific dataset* that you will be using. It is **strongly recommended** that you try to find a dataset that is either a CSV or Excel (.xlsx) file, but if you find a dataset that you are excited to use and it is not in one of those formats, **contact your instructor** to check and see if it will be possible for you to load that dataset in a Jupyter Notebook using the tools we've learned about in class. Datasets in the form of an SQL database are not good options for this course, unless you already have the skills necessary to work with such a database. 

---
# Example Submission

## Research Question 

#### “What are the odds the Detroit Lions will beat the Green Bay Packers on December 13th?”

## Resources 
- I will construct an Elo Model in Python, which will be based on the [code provided here.](https://www.kaggle.com/kplauritzen/elo-ratings-in-python) 
- After I’ve built my Elo model, I will use the [win-loss record of the two teams](https://www.footballdb.com/games/index.html) to make a prediction about the specific game on December 13th. The specific dataset I will use is included in my submission, titled *"Example_Football_Dataset.csv".*
