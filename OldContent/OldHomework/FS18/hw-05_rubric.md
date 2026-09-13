# CMSE 201 - Homework 5 Rubric

In this homework assignment, students are primarily expected to practice their
pandas data manipulation skills and their NumPy `polyfit` and SciPy `curve_fit`
proficiencies. In particular, students will be working with a CSV file where
they will have to mask and sort the data to extract information and they will use
`polyfit` and `curve_fit` to fit data for a simple population model. The biggest
struggle will likely be figuring out how to mask the Pandas dataframe appropriately.

The total number of points possible in this assignment is: **35**

## Part 1: Exploring the cost of Avocados (21 points)

### Loading and inspecting the data (3 points)
* The student should receive:
  - **1 point** for successfully loading the data with pandas
  - **1 point** for using Pandas functions to extract information
  - **1 point** for answering the questions about the properties of the dataset

### Determining the cheapest and most expensive regions to buy avocados (4 point)
* The student should receive:
  - **2 points** *each* for correctly determining the regions, cost, and date for:
    1. The most expensive avocados (2 points)
    2. The least expensive avocados (2 points)

### Tallying total avocado sales (4 points)
* The student should receive:
  - **1 point** *each* for determining the total number of avocados for each variety (3 points total)
  - **1 point** for correctly stating which type of avocado was sold the most

### Visualizing avocado cost trends (7 points)
* The student should receive:
  - **3 points** for the correct first plot (including labels, title, and seaborn styling)
  (partial credit can be given for getting some but not pieces of the plot right)
  - **3 points** for the correct second plot (including labels, title, and seaborn styling)
  (partial credit can be given for getting some but not pieces of the plot right)
  - **1 point** for answering the question about whether or not their plots agree
  with the article.

### Looking for correlations (3 points)
* The student should receive:
  - **1 point** for making the `jointplot`
  - **1 point** for addressing whether or not their results are correlated
  - **1 point** for commenting on whether or not the points on the low end are
  biasing their results and making an attempt to check this

## Part 2: Revisiting the Population Model (14 points)

### Loading the popuation data (2 points)
* The student should receive:
  - **1 point** for loading the data with Pandas.
  - **1 point** for making sure the first row isn't read as a header

### Define the model function and using `curve_fit` (7 points)
* The student should receive:
  - **1 point** for defining the correct population function
  - **1 point** for using the population function with `curve_fit` to get parameters
  - **2 points** for using the right parameters in a call to the population function
  to get the predicted values
  - **1 point** for making the plot
  - **1 point** for answering the first question
  - **1 point** for answering the second question

### Trying to use `polyfit` instead (5 points)
* The student should receive:
  - **1 point** for using `polyfit` correctly
  - **1 point** for using `poly1d` correctly to create a new functions
  - **1 point** for using the function from `poly1d` correctly
  - **1 point** for making the plot
  - **1 point** for explaining their choice of polynomial order.
