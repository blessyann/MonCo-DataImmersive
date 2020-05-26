# Exercise 7.1 Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car such as, 
# "Let me see if I can find you a Subaru."

message = input("what kind of rental car you would like: ") 
print(message)
print(f"\n Let me see if I can find a {message.title()}")

# Exercise 7.2 Restaurant Seating: Write a program that asks the user how many people are in their dinner group. 
# If the message is more than eight, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.

msg = input("\nHow many people are in your dinner group :")
if int(msg) > 8:
    print("\n Please wait for a table")
else:
    print("\n Your table is ready!!")

