# Exercise 5.1 Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test

car = 'subaru'
print("\nIs car == 'subaru'? I predict True")
if car in 'subaru':
    print("true")
print("Is car == 'audi'? I predict false")
if car in 'audi':
    print("true")
else:
    print("false")

# Exercise 5.2 More Conditional Tests: 

num = 32
car = 'subaru' 'audi'
if num <= 50:
    print(" Num value is less than 50")
else:
    print(" Num value is greater than 50")
if num <=50 and num >=40:
    print("Num value is between 40 to 50")
elif num <= 50 and num >=30:
    print("Num value is between 30 and 50")
print("Using lower() function")
if car == car.lower():
    print("true")

# Exercise 5.3 Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called "alien_color" and assign it a value of 'green', 
#'yellow', or 'red'. Write an "if" statement to test whether the alien's color is green. If it is, print a message that they player has earned 5 points. 
# Write one version of this program that passes the "if" test and another that fails.

alien_colors = ['green','red','yellow']
#alien_color = 'green'
alien_color = 'red'
if alien_color == 'green':
    print(" \n The player earned 5 points")
else:
    print("\n The player earned 10 points")

