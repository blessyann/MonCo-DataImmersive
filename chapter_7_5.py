# Exercise 7.5 Movie Tickets: A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop that asks users their age, and then tell them the 
# cost of their movie ticket.

msg = input("Please Enter the age: \t")
if int(msg) < 3:
    print("\n Ticket is free under age 3")
elif int(msg) < 12:
    print("\n Ticket charge is $10")
else:
    print("\n Ticket charge is $15")