# Number Guessing Game
A simple number-guessing game where you set a range and try to guess a randomly chosen number.
Use the binary search strategy to find the number in the fewest possible guesses.

How It Works
Set your range by choosing a lower and upper limit.
The game picks a random number within that range.
It calculates the ideal number of guesses needed using binary search.
Start guessing. The game will tell you if your guess is too high or too low.
Try to stay within the ideal number of guesses for a perfect score.
Example
typescript
Copy
Edit
Start by picking your range.  
Lower limit: 1  
Upper limit: 100  
Ideal number of guesses: 7  

Guess: 50  
The number is higher.  
Guess: 75  
The number is lower.  
Guess: 62  
The number is higher.  
...  
You guessed the number!  
Total number of guesses: 6  
Congratulations! You were within the ideal number of guesses!  
How to Run
Make sure you have Python installed, then run:

sh
Copy
Edit
python game.py
Can You Beat the Ideal Guess Count?
Use strategy, think smart, and see if you can guess efficiently.
