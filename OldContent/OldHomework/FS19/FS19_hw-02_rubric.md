# CMSE 201 - Homework 2 Rubric

In this homework assignment, students are primarily expected to practice their
writing loops, writing custom functions, making multi-panel plots with matplotlib,
and using a few built-in NumPy functions. Note that they will have only very recently
been exposed to NumPy.

The total number of points possible in this assignment is: **29**

* The student should receive:
  - **1 point** for successfully using loop function.
  - **1 point** for successfully appending the effective mass in a new list .
  - **1 point** for getting the average and round correctly.


## Part 1: Where do samples come from? (12 points)

### Question 1 (1 point)

* The student should receive:
  - **0.5 points** for correctly stating that it is a dictionary.
  - **0.5 points** for writing the command to retrieve the activity of chromosome 6 in the 5 samples.

### Question 2 (1 point)

* The student should receive:
  - **0.5 points** for correctly importing pyplot from matplotlib.
  - **0.5 points** for writing the inline command.

### Question 3 (2 points)

* The student should receive:
  - **1 point** for drawing the histogram.
  - **0.5 points** for adding x- and y-labels and a title.
  - **0.5 points** for adding rwidth and alpha parameters.

### Question 4 (3 points)

* The student should receive:
  - **2 points** for drawing the two histograms in the same plot (overlapping).
      - Only **1 point** if the two histograms are in two different plots.
      - Only **1 point** if the two histograms are in the same plot but are not transparent.
  - **1 point** for adding the bins parameter assigned to new_bins.

### Question 5 (3 points)

* The student should receive:
  - **2 points** for calling the `plot_panel_two_hist` function for all four chromosomes (0.5 points per line).
  - **1 point** for correctly explaining the `figsize` and `tight_layout` parameters (0.5 points each).

### Question 6 (1 points)

* The student should receive:
  - **1 point** for correctly pointing out that ChrY is able to distinguish between female/male samples.

### Question 7 (1 point)

* The student should receive:
  - **1 point** for correctly pointing out that the first and second samples are likely to be female and the last three samples are likely to be male.


## Part 2: Exploring a fundamental theorem in probability/statistics (17 points)

### Question 8 (1 points)

* The student should receive:
  - **1 point** for correctly importing `numpy` as `np`.

### Question 9 (2 point)

* The student should receive:
  - **0.5 points** for drawing the histogram showing a power-law distribution.
  - **0.5 points** for adding rwidth and alpha parameters.

### Question 10 (2 point)

* The student should receive:
  - **1 point** for correctly printing the mean and std.dev of the 1000 numbers (0.5 points for each).
  - **1 point** for correctly printing the mean of the random draw.

### Question 11 (4 point)

* The student should receive:
  - **1 point** for correctly defining the function `rand_draw_averages` with the three arguments `input_list, draw_size, num_draws`.
  - **1 point** for correctly calculating using the `sample` function `sample(input_list, draw_size)`.
  - **1 point** for correctly calculating the mean of each draw: `mean_of_random_draw = np.mean(sample(input_list, draw_size))`.
  - **1 point** for correctly writing the `for` loop to iterate `num_draw` times, appending the mean each time, and returning the `draw_avgs` list.

### Question 12 (2 points)

* The student should receive:
  - **1 point** for correctly calling the `rand_draw_averages` function.
  - **1 point** for correctly plotting the histogram.

### Question 13 (2 points)

* Comment: The line `chr = all_chromosomes[k]` is there by mistake but makes no difference. So, please ignore.
* The student should receive:
  - **1 point** for correctly writing comments about the first 3 lines inside the for loop.
  - **1 point** for correctly writing comments about the `i` and `j` plot indices and the `plot_panel_hist` call.

### Question 14 (1 points)

* The student should receive:
  - **1 point** for correctly describing the observation that as the size of the random draw increases, the distribution of averages resembles the bell curve more and more.

### Question 15 (3 points)

* The student should receive:
  - **1 point** for correctly using the `subplots` function to create two plot panels side-by-side.
  - **0.5 point** for correctly plotting the histogram of means.
  - **0.5 point** for correctly plotting the histogram of std. deviations.
  - **1 point** for correctly pointing out that the mean of the averages is really close to the average of the original distribution and that the std. dev. of the averages decreases with increasing draw sizes. 
