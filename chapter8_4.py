# Exercise 8.4  Large shirts: Modify the "make_shirt()" function so that shorts are large by default with a message that reads, "I love Python". 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size ='L',text='I love Python'):
    print(f"\n the sizt of shirt is :- {size}")
    print(f"\n The text printed on the shirt is:- {text}")
    
make_shirt('s','yo yo')
make_shirt('m')
make_shirt()
