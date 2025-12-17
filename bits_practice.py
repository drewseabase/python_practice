name = input("What is your name? ")
age = int(input("Enter your age: "))
random_num = int(input("Enter a random number: "))
current_year = 2025
number = 0

calc_year = (current_year - age) + 100

while random_num != number:
    print(f'Hi {name}, you are currently {age} and you will turn 100 in the year {calc_year}')
    number += 1

