# Exercise 5.5 Alien Colors #3: Turn your "if-else" chain from Exercise 5.4 into an "if-elif-else" chain. If the alien is green, 
# print a message that the player earned 5 points. If the alien's color is yellow, print a message that the player earned 10 points. 
# If the alien is red, print a message that the player earned 15 points. Write three versions of this program,
# making sure each message is printed for the appropriate color alien.

print("\n Stages of Life")
age = 10
if age <= 2:
    print("The person is a Baby\n")
elif age <= 4:
     print("The person is a Toddler\n")
elif age <= 13:
     print("The person is a kid\n")
elif age <=20:
     print("The person is a Teenager\n")
elif age <=65:
     print("The person is an Adult\n")
else:
     print("The person is an Elder\n")

