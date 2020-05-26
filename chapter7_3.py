# Exercise 7.3 Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

message = input("\nPlease enter a number:\t ") 
if int(message) % 10 == 0:
    print(f"The enterd number {message} is the multiple of 10 \n ")
else:
    print(f"The enterd number {message} is not the multiple of 10 \n ")
