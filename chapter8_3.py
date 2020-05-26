# Exercise 8.3 T-shirt: Write a function called "make_shirt()" that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt(size = 'L',text = 'I love USA'):
    print(f"\n the sizt of shirt is :- {size}")
    print(f"\n The text printed on the shirt is:- {text}")
    
make_shirt('L','super boyz')
make_shirt()
