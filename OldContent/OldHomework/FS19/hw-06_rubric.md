# CMSE 201 - Homework 6 Rubric


The total number of points possible in this assignment is: **48**

### Question 1 (2 points)

* The student should receive:
  - **1 point** for loading the data with Pandas
  - **1 point** for correctly separating x and y

### Question 2 (4 points)

* The student should receive:
  - **2 points** for making a scatter plot (either with `scatter` or a plot with no connected dots)
  - **2 points** for correctly labeling each axis

### Question 3 (2 points)

* The student should receive:
  - **2 points** for recognizing two different features (e.g. large scale behavior and small scale behavior)

### Question 4 (8 points)

* The student should receive:
  - **2 points** for each of the four bullet points

### Question 5 (4 points)

* The student should receive:
  - **2 points** for printing the parameters
  - **2 points** for giving a reasonable answers w.r.t to the goodness of the fit

### Question 6 (4 points)

* The student should receive:
  - **2 points** for correctly trying and visualizing a higher order polynomial
  - **2 points** for giving _any_ viable explanation for their choice.

### Question 7 (8 points)

* The student should receive:
  - **2 points** for defining a reasonable function
  - **2 points** for correctly feeding their function into `curve_fit()`
  - **2 points** for correctly leverage `p0` to get a reasonable fit
  - **2 points** for visualizing the data along with the model (regardless of how good the fit is, i.e. if they didn't get `p0` working) 

### Question 8 (2 points)

* The student should receive:
  - **2 points** for giving a thoughtful answer

### Question 9 (1 points)

* The student should receive:
  - **1 point** for clearly stating which parameters they will try to estimate with MCMC

### Question 10 (1 points)

* The student should receive:
  - **1 point** for correctly calculating sigma

### Question 11 (12 points)

* The student should receive:
  - **2 points** for correctly initializing their free and fixed parameters
  - **1 point** for correctly define the number of steps
  - **1 point** for correct defining the step size (or justifying why they changed it from the default)
  - **4 points** for correctly implementing the MCMC algorithm (should involve taking the step the right way, computing chi-squared, calculating the probability, and accepting and rejecting steps)
  - **2 points** for the "random walk" plot
  - **2 points** for the histogram + contour combo