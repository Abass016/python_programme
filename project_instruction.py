#import random
# ask for the users name
# use an input functon their name
# tell the user what they are doing

# secret random.random.random.int(1, 100)

# for loop with a rane between 1, 6:
   # tell the user to guess
   # if statement to check if ythe user input == secret
   # if thr guess is low then print your guess is too low
   # if it is too high then print your guess is too high

#if guess == secret
    #print good job, name, you have the secret num in num_of_tries gueses
#else:
    # print (you guess incorrecty, the sectet nunmber is secret)

# This code asked a user to guess a number correctly

import random

print("Enter your name")

name = input()

print(f"You are asked to guess a number correctly, {name}")
secret_code =  random.randint(1, 10)

for trial in range(1, 6):
    print("Guess the number")
    Guess = int(input())
    if Guess < secret_code:
        print("Your number is low")

    elif Guess > secret_code:
        print("Your number is high")
        
    elif Guess == secret_code:
        print("you have entered the number correctly " + name)
        break

if Guess == secret_code :
    print("Good Job " + name +  " You have the secret number in " + str(trial) + " guess")  

else:
    print("You guess incorrectly, the secret num is %s " % (secret_code) )
