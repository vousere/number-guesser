import random
from time import sleep


user_or_computer = input("Who should guess the number (u) for user,(c) for computer: ").lower()
if user_or_computer == "c":
    tries = 3
    guessed_numbers = []
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))
    number = int(input("What's your number: "))
    if number>max_value or number<min_value:
        number = int(input("Please enter a number between min and max value: "))
    while tries>0:
        sleep(1)
        guess = random.randint(1,10)
        hint_number = [number+1,number-1]
        if guess == number:
            print(f"Congratulations! You guessed right! {number} was my number.")
            print(f"Other guessed numbers: {guessed_numbers}")
            break
        elif guess in hint_number:
            tries = tries-1
            guessed_numbers.append(guess)
            print(f"{guess} is so near!,left {tries} tries.")
        elif guess in guessed_numbers:
            tries = tries+1
        else:
            tries = tries -1
            guessed_numbers.append(guess)
            print(f"Computer's guess: {guess}, left {tries} tries.")

elif user_or_computer == "u":
    tries = 3
    guessed_numbers = []
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))
    number = random.randint(min_value, max_value)
    hint_number = [number+1,number-1]
    while tries>0:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print(f"You caught number on {4-tries}. try,congratulations!\nOther guessed numbers: {guessed_numbers}")
            break
        elif guess in guessed_numbers:
            print(f"You already guessed this number!")
        elif guess in hint_number:
            print(f"{guess} is so near! Keep going.")
        else:
            tries = tries-1
            guessed_numbers.append(guess)
            print(f"You left {tries} tries.")

else:
    print("Invalid,please enter again.")

