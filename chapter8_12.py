# Exercise 8.12 Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich being ordered. 
# Call the function three times, using a different number of arguments each time.

def sandwich(*addon):    
    print(addon) 
    
sandwich('cheese')
sandwich('cheese','tomato') 
sandwich('grilled chicken','olives','sauce')

      

