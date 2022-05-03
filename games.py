print("Welcome to OnlineGames.com")

import random

import time

choice = int(input(
    "Please choose from the following\n1.Lotto Game\n2.Number Guesser\n3.Download Time Converter\n4.number to binary converter"))

if choice == 1:
    print("welcome to the Lotto Game")
    count = 10

    n1 = int(input("1st Pick"))
    n2 = int(input("2nd Pick"))
    n3 = int(input("3rd Pick"))
    n4 = int(input("4th Pick"))
    n5 = int(input("5th Pick"))
    n6 = int(input("6th Pick"))
    n7 = int(input("7th Pick"))

    l1 = random.randint(1, 35)
    l2 = random.randint(1, 35)
    l3 = random.randint(1, 35)
    l4 = random.randint(1, 35)
    l5 = random.randint(1, 35)
    l6 = random.randint(1, 35)
    l7 = random.randint(1, 35)
    l8 = random.randint(1, 35)

    while count != 0:
        print(count)
        count -= 1
        time.sleep(0.5)
    print("Your numbers:", n1, n2, n3, n4, n5, n6, n7)
    print("Winning numbers:", l1, l2, l3, l4, l5, l6, l7)

if choice == 2:
    print("Welcome to the number guessing game\ncan you guess what the computer is thinking between 1-35")
    computer = random.randint(1, 35)
    guess = int(input("Guess:"))
    turns = 0

    while guess:
        if guess < computer:
            print("number is higher")
            turns += 1
            guess = int(input("Guess:"))
        if guess > computer:
            print("number is lower")
            turns += 1
            guess = int(input("Guess:"))
        if guess == computer:
            print("you got it in", turns, "goes")
            break
        if turns == 5:
            print("out of turns")
            print("GAME OVER")
            break

if choice == 3:
    print("Welcome to the download time converter")
    file_type = str(input("GB or MB"))
    file_size = int(input("Enter Size"))
    speed = float(input("Enter Speed"))

    # Formulas
    gbformula_seconds = file_size * 1000 * 8 / speed
    gbformula_minutes = gbformula_seconds / 60
    gbformula_hours = gbformula_minutes / 60
    mbformula_seconds = file_size * 8 / speed
    mbformula_minutes = mbformula_seconds / 60
    mbformula_hours = mbformula_minutes / 60

    while file_type:
        if file_type == "gb" or file_type == "GB":
            print("Seconds:", gbformula_seconds)
            print("Minutes", gbformula_minutes)
            print("Hours", gbformula_hours)
            file_type = str(input("GB or MB"))
            file_size = int(input("Enter Size"))
            speed = float(input("Enter Speed"))
        if file_type == "mb" or file_type == "MB":
            print("Seconds", mbformula_seconds)
            print("Minutes", mbformula_minutes)
            print("Hours", mbformula_hours)
            file_type = str(input("GB or MB"))
            file_size = int(input("Enter size"))
            speed = float(input("Enter Speed"))

if choice == 4:
    print("Welcome to number to binary converter")
    number = int(input("enter a number:"))

    while number:
        x = bin(number).replace("0b", "")
        print("Binary Value =", x)
        number = int(input("enter a number:"))






