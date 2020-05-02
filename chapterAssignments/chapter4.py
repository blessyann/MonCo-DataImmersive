# Exercise 4.1 Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a "for" loop to print the name 
# of each pizza. Modify your loop to print a sentence using the name of the pizza. For each pizza, 
# have one line of output containing a statement such as, "I like pepperoni pizza." Add a line at 
# the end of the program, outside of the "for" loop, that states how much you like pizza. 
# The output results should have the three lines for your favorite types of pizza, and then the 
# additional line at the end stating, "I really love pizza!"

pizzas = ['pepperoni','cheese','vegetable']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I like " +pizza.title()+ " pizza \n")
print("I really love Pizza \n")

# Exercise 4.2 Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a "for" loop to print out the name of each 
# animal. Modify your program to print a statement about each animal such as, "A dog would make a great 
# pet." Add a line at the end of your program stating what these animals have in common. You could 
# print a sentence like, "Any of these animals would make a great pet!"

animals = ['cat', 'dog', 'fish']
for animal in animals:
    #print(animal)
    print(f" A " + animal.title() + " would make a great pet \n")
print("Any of these animals would make a great pet!")

# Exercise 4.3 Counting to Twenty: Use a "for" loop to print the numbers from 1 to 20, inclusive.

for value in range(1,20):   
     print(value)

# Exercise 4.4 One Million: Make a list of the numbers from one to a million, and then use a "for" 
# loop to print the numbers. (If the output is taking too long, use ctrl + C or close the 
# terminal/Powershell window).

 
#for value in range(1, 1000000):    
    #print(value)


# Exercise 4.5 Summing a Million: Make a list of the numbers from one to a 
# million and then use "min()" and "max()" to make sure your list actually starts 
# at one and ends at one million. Also, use the "sum()" function to see
# how quickly Python can add a million numbers.

values = [value for value in range(1, 1000000)] 
#for value range(1, 1000000): 
#print(values) 
print("\n Minimum value in the list")
print(min(values))
print("\n Maximum value in the list")
print(max(values))
print("\n Sum of million numbers ")
print(sum(values))

# Exercise 4.6 Odd Numbers: Use the third argument of the "range()" function 
# (step, which sets by how much you want to increase each number) to make a list 
# of odd numbers from 1 to 20. Use a "for" loop to print out each number.

odd_numbers = list(range(1,20,2))
print("\n odd numbers from 1 to 20 are") 
for odd_number in odd_numbers:
    print(odd_number)

# Exercise 4.7 Threes: Make a list of the multiple of 3, from 3 to 30. Use a "for"
# loop to print the numbers in your list.

threes = []
print("\nlist of the multiple of 3, from 3 to 30")
for value in range(3,30):
    three = value*3     
    #threes.append(three)
    print(three)

# Exercise 4.8 Cubes: A number raised to the third power is called a "cube". 
# For example, a cube of 2 is written as 2**3 in Python. Make a list of the first 
# ten cubes (that is, the cube of each integer 1 to 10), and use a "for" loop to 
# print out the value of each cube.

cubes = []
print("\nlist of the first ten cubes ")
for value in range(1,10):
    cube = value**3     
    #threes.append(three)
    print(cube)

# Exercise 4.9 Cube Comprehension: Use a list comprehension to generate a list of
# the first ten cubes.

print("\ncube comprehension")
cubes = [value**3 for value in range(1,10)] 
print(cubes)

# Exercise 4.10 Slices: Using one of the programs in the previous exercises, add 
# several lines to the end of the program that do the following tasks - 1) Print 
# the message, "The first three items in the list are:", then use a list slice to 
# print the first three items from that program's list. 2) Print the message, 
# "Three items from the middle of the list are:", and use a slice to print three 
# items from the middle of the list. 3) Print the message, "The last three items 
# in the list are:" and use a slice to print the last three items in the list.

print("\nThe first three items in the list cubes are:")
print(cubes[0:3])
print("Three items from the middle of the list are:")
i = len(cubes)/2
print(cubes[int(i): int(i+3)])
print("The last Three items  of the list are:")
i = len(cubes)-3
print(cubes[int(i): int(len(cubes))])

# Exercise 4.11 My Pizzas, Your Pizzas: Start with your program from Exercise 4.1. 
# Make a copy of the list of pizzas and call it "friend_pizzas". Then do the 
# following: 1) Add a new pizza to the original list. 2) Add a different pizza to 
# the list of "friend_pizzas". 3) Prove that you have two separate lists. Print 
# the message, "My favorite pizzas are:", then use a "for" loop to print the first 
# list. Print the message, "My friend's favorite pizzas are:", then use a "for" 
# loop to print the second list. Make sure each new pizza is stored in the 
# appropriate list.

print("\nCopy of pizza list")
friend_pizzas = pizzas[:]
print(friend_pizzas)
pizzas.append('mixed')  
friend_pizzas.append('sea food')
print(pizzas)
print(friend_pizzas)
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

