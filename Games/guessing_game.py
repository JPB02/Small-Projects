from random import choice

random_num = choice(range(1,101))

print("Input a number between 1 and 100:")
user_input = int(input())

while user_input != random_num:
    if user_input < random_num:
        print("Your guess is too low!")
        user_input = int(input())
    else:
        print("Your guess is too high!")
        user_input = int(input())
print("You guessed it!\nThe correct number was:",random_num)