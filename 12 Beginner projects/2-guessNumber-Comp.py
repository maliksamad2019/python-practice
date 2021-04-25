import random

def guess(x):
    random_Number = random.randint(1,x)
    guess = 0

    while guess != random_Number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_Number:
            print("Sorry, guess again. Too low.")
        elif guess > random_Number:
            print("Sorry, guess again. Too high.")

    print(f"Yay, Congrats, you have guessed the number {random_Number} correctly.")

def computerGuess (x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c' and low <= high:
        if low != high:
            guess = int(random.randint(low,high))
        else:
            guess = low

        feedback = input(f"Is {guess} too High (h), too Low (l), or Correct (c)?? ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1

    print(f"Yay, Congrats, Computer have guessed the number {guess} correctly.")


    

computerGuess(20)