import random
import math

#User sets their lower and upper bounds
print("Start by picking your range.")
print("Hint: Use binary search to optimize you search by always guessing the middle number")
lower_limit = int(input("Lower limit: "))
upper_limit = int(input("Upper limit: "))
target_number = random.randint(lower_limit, upper_limit)

#Python gets the range and gives the user the ideal number of searches
N = upper_limit - lower_limit + 1
ideal_guesses = math.ceil(math.log(N, 2))
print(f"Ideal number of guesses: {ideal_guesses}")
print("Now guess a number in the range of your limits.")

#Tracks the number of guesses the user input
guess_count = 0 

def output_protocol():
  global guess_count
  guess_count += 1
  x = 0
  x = int(input("Guess: "))
  
  if x > upper_limit or x < lower_limit:
    print("Enter a number in the correct range.")
    output_protocol()
  
  elif x > target_number:
    print("The number is lower.")
    output_protocol()

  elif x < target_number:
    print("The number is higher.")
    output_protocol()

  elif x == target_number:
    print("You guessed the number!")

  else:
    print("You can only enter a number!")

#Python gives the user their results
output_protocol()
print(f"Total number of guesses: {guess_count}")

if guess_count > ideal_guesses:
  print("Oh no! You exceeded the ideal number of guesses.")
else:
  print("Congratulations! You were within the ideal number of guesses!")
  