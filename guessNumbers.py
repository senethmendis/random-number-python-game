#nnumber guessing game
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        # cast the input to integers user * int() *
        guess = int(input(f"Guess a Number 1  and {x} : "))
        if guess < random_number:
            print("Try Again the Number is Too Low!")
        elif guess > random_number:
            print("Try Again the number is Too High!")

    print(
        f"Congrats, You guess the nunmber!!!! the number is : {random_number}")

# the parameter is the randow of the randow numbers
#guess(10)

#play with computer

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too High (H) , too Low (L), Correct (C) : ").lower()

        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f"Yeah , Computer is Correctly guessed {guess} !!!!")

computer_guess(10)