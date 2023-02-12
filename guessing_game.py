import random

def guess_number_game():
  # Generate a random number between 1 and 100
  number = random.randint(1, 100)

  # Ask the user to guess the number
  guess = int(input("Guess a number between 1 and 100: "))

  # Keep track of the number of attempts
  attempts = 1

  # Loop until the user guesses the number
  while guess != number:
    # Give the user a hint
    if guess < number:
      print("It's too low! Try again.")
    else:
      print("It's too high! Try again.")

    # Ask the user to guess again
    guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of attempts
    attempts += 1

  # The user has guessed the number
  print("Congratulations, You've got it in", attempts, "attempts! The number was", number)

# Start the game
guess_number_game()
