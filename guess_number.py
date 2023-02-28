import random
num=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 and 20 :"))
    if guess==num:
        print("You guessed correct number.")
        break
    elif guess>num:
        print("You guessed greater number.")
    elif guess<num:
        print("You guessed smaller number.")
