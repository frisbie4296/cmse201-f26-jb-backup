# CMSE 201 - Homework 4 Rubric



The total number of points possible in this assignment is: **39**

### Question 1 (5 point)

* The student should receive:
  - **1 point** for randint function for x
  - **1 point** for randint function for y
  - **1 point** for if statement checking board[test_x][test_y]
  - **1 point** for if statement checking board[test_x][test_y] != -1
  - **1 point** for setting good_place to False

### Question 2 (5 points)

* The student should receive:
  - **1 point** for always returning 'hit' or 'miss'
  - **1 point** for always returning the board
  - **1 point** for checking board[x_ind][y_ind] not equal to -1
  - **1 point** for checking board[x_ind][y_ind] not equal to 5
  - **1 point** for setting board[x_ind,yind] to 5 if hit

### Question 3 (7 points)

Writing the check_board function:

* The student should receive:
  - **1 point** for defining a sunk list in check_board
  - **1 point** for returning a sunk list
  - **1 point** for if the list is of ship names (as opposed to integer values)
  - **1 point** for using np.isin function correctly

Testing the check_board function:

* The student should receive:
  - **1 point** for calling the shot function and storing the result
  - **1 point** for calling the check_board function and printing the result
  - **1 point** for displaying the board with a sunken ship

### Question 4 (3 points)

* The student should receive:
  - **1 point** for randomly choosing a x value (with correct bounds)
  - **1 point** for randomly choosing a y value (with correct bounds)
  - **1 point** for returning x and y
 
### Question 5 (8 point)

Writing the play_game function:

* The student should receive:
  - **1 point** for incrementing n_steps by 1
  - **1 point** for calling the player_function (not random_player)
  - **1 point** for calling a player function and capturing the x and y guesses
  - **1 point** for passing the x and y guesses to the shot function
  - **1 point** for storing the board from the shot function (in the board variable)

Testing the play_game function:

* The student should receive:
  - **1 point** for writing a for loop that loops 10 times
  - **1 point** for storing the results of play_game in a list
  - **1 point** for printing the average result

### Question 6 (6 points)

Writing the smart_player function:

* The student should receive:
  - **1 point** for randomly picking x and y positions
  - **1 point** for returning x and y positions
  - **1 point** for checking whether these are in the past_guesses list
  - **1 point** for only returning the x and y positions if they aren't in past_guesses

Calling smart_player:

* The student should receive:
  - **1 point** for passing smart_player to play_game
  - **1 point** for obtaining a (significantly) lower average result than for random_player

### Question 7 (5 points)

* The student should receive:
  - **1 point** for acknowledging that smart_player was far from optimal
  - **1 point** for suggesting an approach that takes into account where the hits have been registered so far
  - **1 point** for taking into account the length of the ships that still have not been sunk
  - **1 point** for not saying anything that is obviously false
  - **1 point** for clarity
