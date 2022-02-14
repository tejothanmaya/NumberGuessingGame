import random
print("Nimber Guessing Game")
chances = 0
number = random.randint(1,9)
guess = int(input("Enter your guess:"))
while chances < 5:

 if guess == number:
     print("Congratulations YOU WON!!!!!")
     break
 elif guess>number:
     print("It's too high enter a number less than it")
     break
 else:
     print("Your number is too low enter a number greater than it")
 chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)