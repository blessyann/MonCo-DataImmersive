# Exercise 6.10 Favorite Numbers: Modify your program from Exercise 6.2 so each person can have more than one favorite number. 
# Then print each person's name along with their favorite numbers.

favorite_numbers = {
    'john': [7, 17],
    'lee': [25, 39, 56],
    'mac': [12, 19],
    'cathlin': [22, 44]
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))