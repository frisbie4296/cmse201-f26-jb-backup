#!/usr/bin/env python
# coding: utf-8

# # CMSE 201 Final Project Example B
# ### &#9989; CMSE Student
# ### &#9989; Section_001
# #### &#9989; April 17th, 2021

# # Has the proportion of female STEM majors finally reached equilibrium?

# ## 1 Background and Motivation

# Throughout the early 21st century, there has been a collective push from education organizations, job recruiters, and parents everywhere for college students to enter into the study of science, technology, engineering, and math, or as we cocllectively know them, the "STEM" subjects. There have been increases in funding for STEM departments nationwide, media campaigns aimed towards younger students, and resulting increases in STEM major enrollments (1). But that push was meant to cover for a decades-long deficit of a group of students include in STEM education: women. The STEM fields are known to be male-dominated career fields and are typically higher paying and have higher job longevity, so as a result, a good portion of the STEM push was aimed towards female students. But did it work?
# 
# In this study, we are going to be using hypothesis testing to determine whether or not the proportion of female students in STEM majors is equal to the proportion of female college students overall. Was the long history of a firm male majority in the fields overcome with a few decacdes' worth of encouragement for younger students? Which subjects are more progressive on this front? In 2017, 57% of college students identified as women, as reported by the National Center for Education Statistics (2), so we will establish that as the benchmark the STEM subjects must meet. In order to test the question, we will be using a dataset compiled by FiveThirtyEight by randomly surveying recent (recent of the time, class of 2014 and 2015) graduates on their gender and major (3). We will compare the found sample proportion to the reported NCES parameter before further comparing by subject to answer the question _has the percentage of women in STEM majors reached equilibrium yet?_

# ## 2 Methodology

# We can think of this data situation in terms of proportions, namely the sample proportion (p-hat) taken from the data and the population proportion of 0.57 (p) that is the supposed percentage of female college students. Using these, we can set up a one-proportion hypothesis test with the following hypotheses:

# <center>$H_{o}: \hat{p} = p = 0.57$ <br>
# $H_{a}: \hat{p} \neq p$<center>

# The null hypothesis states that the two proportions are the same, that is that the proportion of female STEM majors is equal to that of female college students, reaching equilbrium. The alternative hypothesis states that the two are not equal; it is important to note that if the null hypothesis is rejected, this will not state which one is greater, as that will require additional analysis to determine. We will test these at the significance level of $\alpha = 0.05$

# ### 2.1 Treating All Subjects as One Population

# Obviously, "STEM" is comprised of a diverse mix of subject areas and proportions will likely vary across them, but to start, we will treat the list of STEM majors as a single population in order to find overarching trends. A snippet of the data is seen below. The variables we will be focusing on are
# 
# - _Major_category_: Which subject each major best corresponds to, this will be used later for classification
# 
# - _ShareWomen_: the percentage of women found by dividing the number of women (variable name "Women") surveyed by the total number surveyed in each major (variable name "Total)

# In[ ]:


import pandas as pd 
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat
get_ipython().run_line_magic('matplotlib', 'inline')

random.seed(5678)

majors = pd.read_csv("stem_breakdown.csv", delimiter = ",")
majors.head(20)


# #### 2.1.1 Analyzing the Distribution

# In order to conduct a hypothesis test, we must first prove that our data qualifies for hypothesis testing in order to assure accuracy in our methods. The cell below creates a function that will return a true value if the data passes the necessary qualifications. Our data passes and we are free to continue testing.

# In[ ]:


def propnorm(dist):
    n = len(dist["ShareWomen"])
    p0 = 0.57
    if n*p0 >= 10 and n*(1-p0)> 10:
        return True
    else:
        return False
propnorm(majors)


# What this means is that even though the population we are working with is not necessarily normal, it is appropriate to use proportion hypothesis testing. Our sample consists of 77 of the most common STEM majors, all of which can be considered instances drawn from the same population. If we were to simulate drawing a great number of these samples (say 1000) from the population, it would begin to resemble a hypothetical normal distribution centered around our population parameter. Hypothesis testing will tell us whether it is possible to draw our sample from that population if the null hypothesis was true and the center was 0.57.

# In[ ]:


x_bar = majors["ShareWomen"].mean()
sigma = majors["ShareWomen"].std()

plt.figure(figsize=(15,10))
plt.subplot(211)
plt.hist(majors["ShareWomen"], bins = 10, color = "green")
plt.xlim(0,1)
plt.axvline(x= x_bar,linewidth=2, color='b')
plt.xlabel("percent women")
plt.ylabel("count")
plt.title("Our Sample - One Sample of 77 Instances With Sample Proportion")
plt.legend(["Mean Sample Proportion"])

plt.subplot(212)
random_dist = np.random.normal(0.57,sigma,size = 1000)
plt.hist(random_dist, bins = 50, color = "grey")
plt.xlim(0,1)
plt.axvline(x= 0.57,linewidth=2, color='r',label = "Mu")
plt.axvline(x= x_bar,linewidth=2, color='b',label = "Sample")
plt.xlabel("simulated percent women")
plt.ylabel("count")
plt.legend(["Population Proportion", "Sample Proportion"])
plt.title("Our population - Many Samples with the Mean Sample Proportion Shown")


# #### 2.1.2 Testing

# Now that we have established a baseline, we can move on to testing. Here, a success is any instance where the proportion of female students (the variable `ShareWomen`) is greater than or equal to our supposed population proportion of 0.57. The cell below runs a z-test command which will output a z-score, p-value, and recommended conclusion. If the proportion rejects the null hypothesis, we will then move forward with creating a 90% confidence interval for a range of possible true proportions. This way, we will be able to determine whether the proportion falls below or above the population proportion. 

# In[ ]:


def test(df):
    successes = sum(df["ShareWomen"] >= 0.57)
    n = len(df["ShareWomen"])
    conclusion = "fail to reject"
    z, p_value = proportions_ztest(successes, n, value = 0.57, alternative = "two-sided")
    if p_value < 0.05:
        conclusion = "reject"
    return z, p_value, conclusion
test(majors)


# In[ ]:


def confint(df):
    n = len(df["ShareWomen"])
    p_hat = df["ShareWomen"].mean()
    z_star = 1.645 #Z star value for a 90% confidence interval
    low = p_hat - z_star*((p_hat*(1-p_hat))/n)**(1/2)
    high = p_hat + z_star*((p_hat*(1-p_hat))/n)**(1/2)
    return low,high
confint(majors)


# ### 2.2 Breakdown by Subject Area

# Next, we can separate the listed STEM majors into five major categories: engineering, physical sciences, life sciences, computer sciences and mathematics, and health sciences.  A small portion of each of the five datasets is shown below. Treating each category as an individual population to draw from, we will repeat the process as used for the overall. The hypotheses remain the same, where the null hypothesis is that the proportion of female STEM students is equal to 0.57 and the alternative is that the proportion is not equal to 0.57.
# 
# We will not reprove that the distributions are eligible for testing, as they are going to be smaller and less likely to follow the rules of larger distributions. However, as they are all subsets of the original dataset, we can proceed with caution and trust the accuracy of our results in relation to the original dataset.

# In[ ]:


engineers = majors.loc[np.where(majors["Major_category"] == "Engineering")]
physci = majors.loc[np.where(majors["Major_category"] == "Physical Sciences")]
compsci = majors.loc[np.where(majors["Major_category"] == "Computers & Mathematics")]
natsci = majors.loc[np.where(majors["Major_category"] == "Biology & Life Science")]
med = majors.loc[np.where(majors["Major_category"] == "Health")]

print(engineers.head())
print(physci.head())
print(compsci.head())
print(natsci.head())
print(med.head())


# In[ ]:


print("Engineering:", test(engineers)) #STD returning as 0 for eng, comp..... yikes
print("Physical Sciences:", test(physci))
print("Computer Sciences/Math:", test(compsci))
print("Natural Sciences",  test(natsci))
print("Health Sciences/Medical:", test(med))


# In[ ]:


print("Engineering:", confint(engineers)) 
print("Physcial Sciences:", confint(physci))
print("Computer Sciences/Math:", confint(compsci))
print("Natural Sciences:",  confint(natsci))
print("Health Sciences/Medical:", confint(med))


# ## 3 Results

# ### 3.1 Overall Results

# In[ ]:


low, high = confint(majors)
plt.figure(figsize=(20,10))
#plt.subplot(121)
plt.hist(majors["ShareWomen"], bins = 20, color = "grey")
plt.axvline(x= x_bar,linewidth=2, color='b',label = "Sample")
plt.axvline(x= 0.57,linewidth=2, color='r',label = "Mu")
plt.xlabel("percent women")
plt.ylabel("count")
plt.title("Plotting the Percentage of Women in Various Majors")
# plt.subplot(122)
# plt.hist(random_dist, bins = 50, color = "green")
# plt.axvline(x= 0.57,linewidth=2, color='b',label = "Mu")
# plt.axvline(x= x_bar,linewidth=2, color='r',label = "Sample")
# plt.xlabel("simulated percent women")
# plt.ylabel("count")
plt.legend(["Population Mean", "Sample Mean"])


# From our z tests, we obtained:
# - _a z-score_: a statistic that measures where the data lies in a realm of feasible answers centered around our population proportion
# - _a p-value_: the probability of getting the results that we did if the null hypothesis was true
# - _a recommended conclusion_: whether to reject or fail to reject the null hypothesis at the significance level of $\alpha =0.05$

# In[ ]:


test(majors)


# The resulting z-score is towards the edge of the acceptable range. Since our p-value (0.00000019776) is much less than our significance level (0.05), we can reject the null hypothesis. There is significant evidence that the proportion of female STEM majors is not equal to the proportion of female college students. This is supported by the confidence interval for the proportion over the entire dataset.

# In[ ]:


confint(majors)


# We can say with 90% confidence that the true proportion of female STEM majors in this dataset is between 34.39% and 52.99% which supports the original conclusion to reject the hypothesis that it is equal to 57%. 0.57 is not included in the interval, which means that it is extremely unlikely for it to be the true proportion. Moreover, both bounds are below the 0.57 mark, suggesting that the true proportion of female STEM students is lower than the proportion of female college students.
# 
# The plot below represents this visually. If we were to simulate repetitions of our data centered around the population parameter of 0.57, it would resemble this graph, with the shaded region representing the proportion of female STEM majors.

# In[ ]:


low, high = confint(majors)
random_dist = np.random.normal(0.57,sigma,size = 1000)
plt.figure(figsize=(20,10))
plt.hist(random_dist, bins = 50, color = "grey")
plt.xlim(0,1)
plt.axvline(x= 0.57,linewidth=2, color='r',label = "Mu")
plt.axvline(x=x_bar, linewidth = 2, color = "b", label = "Sample")
plt.axvline(x= x_bar,linewidth=206, color='lightblue', alpha = 0.5, label = "CI")
plt.xlabel("simulated percent women")
plt.ylabel("count")
legend = plt.legend(["Population Proportion", "Sample Proportion", "Confidence Interval"])
for i in legend.legendHandles:
    i.set_linewidth(5)


# ### 3.2 Subject Results

# The same function was used for the overall results, so we receive the same output: z-score, p-value, conclusion. At the $\alpha = 0.05$ significance level, we fail to reject the null hypothesis for the physical sciences and natural sciences. Both p-values (0.3017 and 0.2012 respectively) are greater than our $\alpha$ so there is no significant evidence to suggest that the proportions of female students in those subjects are different than 0.57. However, at the same confidence level, we can reject the null hypothesis for engineering, computer sciences, and health science students. The p-values in those subjects are all much less than $\alpha$. In fact, the returned p-values for engineering and computer science are so low that the code cannot register it and return an error message. There is practically a 0% probability that the null hypothesis is true.

# In[ ]:


print("Engineering:", test(engineers)) 
print("Physical Sciences:", test(physci))
print("Natural Sciences",  test(natsci))
print("Computer Sciences/Math:", test(compsci))
print("Health Sciences/Medical:", test(med))


# The results become a bit more clear when using the confidence intervals. We can say with 90% confidence that the true proportion are within the ranges below. The two subjects that failed to reject the null hypothesis both contain 0.57 in their intervals, confirming initials suspicions. The engineering interval is nowhere close to 0.57 so the hypothesis for that subject is soundly rejected. Computer and health sciences both contain 0.57 at the tail ends of their intervals, meaning it is possible but incredibly unlikely for the true proportion to be 0.57, so the hypothesis is also rejected. However, it is rejected for a different reason in each case. The engineering and computer science intervals are both significantly below the paramter but health sciences are firmly above the parameter, so the proportion of female students in that subject is not equal but likely has a higher proportion of female students than the general college population.
# We can visualize these results below, where the sample proportions of each subject are plotted against the population proportion and a simulated population.

# In[ ]:


print("Engineering:", confint(engineers)) 
print("Physcial Sciences:", confint(physci))
print("Natural Sciences",  confint(natsci))
print("Computer Sciences/Math:", confint(compsci))
print("Health Sciences/Medical:", confint(med))


# In[ ]:


engmean = engineers["ShareWomen"].mean()
physmean = physci["ShareWomen"].mean()
cscimean = compsci["ShareWomen"].mean()
natsmean = natsci["ShareWomen"].mean()
medmean = med["ShareWomen"].mean()

plt.figure(figsize=(20,10))
plt.hist(random_dist, bins = 50, color = "grey")
plt.xlim(0,1)
plt.axvline(x= 0.57,linewidth=4, color='black')
plt.axvline(x= engmean,linewidth=4, color='r')
plt.axvline(x= physmean,linewidth=4, color='orange')
plt.axvline(x= natsmean,linewidth=4, color='green')
plt.axvline(x= cscimean,linewidth=4, color='blue')
plt.axvline(x= medmean,linewidth=4, color='purple')
plt.xlabel("simulated percent women")
plt.ylabel("count")
plt.legend(["Population Mean", "Engineering Mean", "Physical Sci Mean", "Computer Sci Mean", "Natural Sci Mean", "Health Sci Mean"])
print(engmean, physmean, natsmean, cscimean, medmean)


# In[ ]:


#Confidence intervals
plt.figure(figsize = (15,10))
plt.axvline(x=0.57, color = "black", lw = 4)
plt.plot([confint(engineers)[0], confint(engineers)[1]], [0.1,0.1], color = "red", lw = 10)
plt.plot([confint(physci)[0], confint(physci)[1]], [0.2,0.2], color = "orange", lw = 10)
plt.plot([confint(natsci)[0], confint(natsci)[1]], [0.3,0.3], color = "green", lw = 10)
plt.plot([confint(compsci)[0], confint(compsci)[1]], [0.4,0.4], color = "blue", lw = 10)
plt.plot([confint(med)[0], confint(med)[1]], [0.5,0.5], color = "purple", lw = 10)

#plt.plot([confint(majors)[0], confint(majors)[1]], [0.6,0.6], color = "grey", lw = 10)
plt.text(0.11, 0.11, "0.109 - 0.369, Fails")
plt.text(0.25, 0.21, "0.249 - 0.769, Passes")
plt.text(0.35, 0.31, "0.371 - 0.804, Passes")
plt.text(0.08, 0.41, "0.082 - 0.542, Fails")
plt.text(0.6, 0.51, "0.6032 - 0.987, Fails")
#plt.text(0.35, 0.61 ,"0.344 - 0.530, Fails")
legend2 = plt.legend(["College Proportion", "Engineering", "Physical Sciences", "Natural Sciences", "Computer Sciences/Math", "Health Sciences", "Overall"])
plt.title("Confidence Intervals per Subject")
plt.xlabel("% Women")
for i in legend2.legendHandles:
    i.set_linewidth(3)


# ## Discussion and Conclusion

# Overall, we have significant evidence to reject our initital hypothesis and say that the proportion of female STEM majors is not equal to the proportion of female college students. Given the results of the confidence interval, we are 90% certain that the true proportion lies between 34.4% and 53.0% and can firmly say that the true proportion is below the estimate. Our dataset was very comprehensive, with almost 2 million graduates surveyed accross 77 majors, and it found a mean sample proportion of approximately 43.7%, well below the supposed 57%. 
# 
# On the surface, this is saddening, but the results become a bit more clear when we take the difference in subjects into account. Out of the five subjects, two of them (physical and natural sciences) did not have any significant evidence that the mean was different than the 57%. In actuality, the mean proportion of women in our dataset in the two subjects are about 50.8% and 58.7%, which are not statistically different than the estimated 57%. This means that in the larger college population, female students probably have reached equilibrium in comparison to non-STEM subjects. However, three subjects (health sciences, math and computer sciences, and engineering) did have significant evidence that the proportion of women was different than the population proportion. The real outlier here, albeit an unsprising one, is health sciences where the confidence interval is enough to suggest that the true proportion of female students is above the population average, closer to 79.5% women. On the other hand, both computer sciences and engineering have proportions that are significantly below the mean at 31.1% and 23.9% respectively. So while health sciences are not in equilibirum because women hold a strong majority, engineering and computer sciences are not in equilibrium because women are nowhere close to a majority. If we hold mean proportion of women among majors as the measure of success for each subject, we can rank the subjects from best to worst, in terms of how far the subject is from a balanced 57% proportion.
# 
# <center> 
#     1. Physical Sciences (58.7%, Equilibrium Reached!)
#     
#     2. Natural Sciences (50.8%, Equilbrium Reached!) 
#    
#     3. Health Sciences (79.5%, +22.5%)
#     
#     4. Computer Sciences (31.3%, -25.7%)
#     
#     5. Engineering (23.9%, -28.1%) 
# 
# The effect that the difference in subjects has on the overall result is obvious. With two subjects in the middle, two below, and one above, they all average out below the population proportion. It is also noteworthy that the number of majors per subject is not evenly distributed, with engineering accounting for the most STEM majors, so it makes sense that the data is swayed in that direction. This is not to say that one subject is more responsible for the lackluster proportion than another, and there are extremes within this data. Subject proportions range from less than 8% women in Mechanical Engineering to about 96% women in Communication Disorder Sciences. However, engineering and computer sciences degree are often the most marketable and profitable in the job market these days, which could attribute to the apparent wage gap seen in high-ranking STEM professions (3) and should be looked into more heavily.
# 
# This study is limited in the sense of the data we are working with. While the overall dataset is large enough to warrant testing, each of the subject data frames are a bit smaller and do not provide as many points to establish a baseline. This also means that the smaller datasets have very large standard deviations, as there are majors within each subject that are at one extreme or the other. This means that our confidence intervals are perhaps larger than they should be, but the results would likely be the same. Future exploration into the matter should attempt to include more majors (even if they are less common) in order to account for this issue and create more precise data ranges. Moreover, this dataset is somewhat dated, with the majority of those surveyed graduating with the class of 2014. It is possible that enrollment demographics could have shifted more towards equilibirium in this time, and working with more recent data would create a more complete picture of the state of STEM education.

# ### References

# 1. Emsi. “Stem Majors on the Rise as Humanities Decline Across the Country,” March 20, 2016. https://www.us.ccb/2016/03/20/stem-programs-humanities-in-each-state/. 
# 
# 2. “The NCES Fast Facts Tool Provides Quick Answers to Many Education Questions (National Center for Education Statistics).” https://nces.ed.gov/fastfacts/display.aspid=98#:~:text=Although%20male%20enrollment%20increased%20by,students%20in%202017%20were%20female.
# 
# 3. Casselman, Ben. “The Economic Guide to Picking a College Major.” FiveThirtyEight (blog), September 12, 2014. https://fivethirtyeight.com/features/the-economic-guide-to-picking-a-college-major/.

# In[ ]:




