# Exercise 7.4 Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you'll add that topping to their pizza.
# Exercise 7.6 Three Exists: Write different versions of either Exercise 7.4 or 7.5 that do each of the following at least once:
# Use a conditional test in the "while" statement to stop the loop.
# use an "active" variable to control how long the loop runs.
# Use a "break" statement to exit the loop when the user enters a 'quit' value.


prompt = "\nEnter the pizza toppings you want :" 
prompt += "\nEnter 'quit' to end . "
message = ""
active = True
while active:    
    message = input(prompt) 
    if message != 'quit':  
        print(f"---{message} is added to your pizza")
    else:
        active = False
        break
    
