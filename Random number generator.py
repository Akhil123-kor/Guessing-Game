import random
number=random.randint(1,10)
chances=0
while chances < 5:
    print("Guess a number(Between 1 and 10, it can also be 1 or 10)")
    answer=int(input("Enter your guess"))
    print("Are you sure?")
    print("Just in case you aren't, I will give you one more chance")
    guess=int(input("Enter your final guess"))
    
    if guess == number:
        print("Congratulations!!! You won!!!")
        chances=chances+1
        break

    elif guess > number:
        print("Your guess was to high: Guess a number lower than", guess)

    else:
        print("Your guess was to low: Guess a number higher than", guess)
        chances=chances+1

if not chances < 5:
    print("You Lose !!! The number is", number)
