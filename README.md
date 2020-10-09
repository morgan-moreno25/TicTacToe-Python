# Tic Tac Toe

This project was completed as Milestone Project 1 for [this course](https://www.udemy.com/course/complete-python-bootcamp/) by Jose Portilla on Udemy.

---

## OVERVIEW

This purpose of this project was to implement what I have learned from the sections leading up to this project.
Those sections include:
    
    - Python Object and Data Structure Basics
    - Python Comparison Operators
    - Python Statements
    - Methods and Functions

Having previous OOP experience, I felt more comfortable implementing this game using Classes to divide the project up into 3 seperate objects:

- The Player Object
    - Used to store and keep track of player names and markers
    - Only 1 method, which is used to prompt the player to pick a position to place their move
- The Board Object
    - Uses a list to store positions in an ordered fashion
    - Their are 2 methods related to a board to the user ( `display` and `walkthrough` )
    - 2 methods related to placing a move at a position on the board ( `place_move` and `validate_move` )
    - The final method ( `is_full` ) checks whether or not every position (excluding the placeholder at position 0) has been played on.
- The Game Object
    - Contains all variables for use in game logic
    - Most methods on this object are simply helper methods for the main method
    - Main method (`play_game`): This method contains all logic pertaining to the game itself being played.

After I created these three classes, I stored an instance of the `TicTacToe` class inside the `Game` variable and called the `play_game` method to begin the game!

---

## Technology

    - Python

---

## What I Learned

From completion of this project, I gained experience in the following:

    - Python Classes
    - Working with user input in Python
    - Using the sleep method from the time library to create pauses in code execution for more fluid gameplay.
    - Python Functions
    - Python Control Flow using If/Elif/Else Statements, For Loops, and While Loops 

---

