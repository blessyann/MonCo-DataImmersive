# Exercise 3.1
# Names: Store the names of a few of your friends in a list called "names". 
# Print each person's name by accessing each element in the list, one at a time.
names = ["John", "Tom", "Jim", "Eric","Erin", "Leo"]
print(names)
names.sort()
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

# Exercise 3.2
# Greetings: Using the list from Exercise 3.1, print a message for each person in your list. 
# The text of the message should be the same, 
# but each message should be personalized with the person's name.
message= "God Bless You "
print(message + names[0])
print(message  + names[1])
print(message  + names[2])
print(message  + names[3])
print(message  + names[4])
print(message  + names[5])


# Exercise 3.3
# Your Own List: Think of a category of things you like, 
# such as types of cars (Toyota, Honda, Ford) or foods (Indian, Chinese, Italian), 
# and make a list that stores several examples. 
# Use your list to print a series of statements about these items such as, 
# "I would like to own a Honda car."
foods = ["Indian","Chinese","Mexican","American"]
print("I would like to eat " + foods[0] + " breakfast") 
print("I would like to eat " + foods[1] + " Lunch") 
print("I would like to eat " + foods[3] + " Dinner") 

# Excercise 3.4
# Guest List: If you could invite several famous people (living or deceased) to dinner, 
# who would you invite? Make a list that includes at least three people, 
# then print a message to each person to invite them to dinner.
gustlist = ["Binu","Sam","Lee","Jack"]
message = " I would like to invite you to our Dinner party"
print("Hi " + gustlist[0] + message ) 
print("Hi " + gustlist[1] + message ) 
print("Hi " + gustlist[3] + message ) 

# Excercise 3.5
# Changing Guest List: You just heard that one of your guests can't make dinner, 
# so you need to send out a new set of invitations. 
# You'll have to think of someone else to invite. 
# Start with the program from Exercise 3.4, 
# and add a print statement to say which guest can't make the dinner. 
# Modify the list, replacing the name of the guest that can't make it with the new invited person. 
# Finally, print a second set of invitation messages, one for each person invited to dinner.
message = "Hi Everyone Lee couln't attend the Dinner Party"
gustlist[2] = "Eric"
print(gustlist)
message = " Dont forget the Dinner party "
print("Hi " + gustlist[0] + message ) 
print("Hi " + gustlist[1] + message ) 
print("Hi " + gustlist[2] + message ) 
print("Hi " + gustlist[3] + message ) 

# Excercise 3.6
#  More Guests: You found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner. 
# Using the program from Exercise 3.5, 
# add a print statement letting your guests know that you have a bigger table. 
# Use the "insert()" function to add one new guest to the beginning and middle of your list, 
# and the "append()" function to add a guest to the end of the list. 
# Print a new set of invitations, one for each person in your list.
message = "\n Hi Everyone More tables avilable in Dinner Party \n"
print(message)
gustlist.insert (0, "Jim")
gustlist.insert (2, "sue")
print(gustlist)
gustlist.append("Liz")
print(gustlist)
message = " Dont forget the Dinner party on Monday"
print("\nHi " + gustlist[0] + message ) 
print("Hi " + gustlist[1] + message ) 
print("Hi " + gustlist[2] + message ) 
print("Hi " + gustlist[3] + message )
print("Hi " + gustlist[4] + message )
print("Hi " + gustlist[5] + message )
print("Hi " + gustlist[6] + message )

# Excercise 3.7
#  Shrinking Guest List: You found out that the new table can't be delivered in time, 
# and you only have space for two guests. 
# Using the program from Exercise 3.6, 
# add a new line that prints a statement that you can only have two guests at dinner. 
# Use the pop() function to remove guests one at a time until only two guests remain. 
# Each time you pop a name from the list, 
# print a message to the person to apologize for not inviting them to dinner. 
# Print a message to the two people still left on your list, 
# letting them know that they are still invited. 
# Use the "del" function to remove the last two names from your list, so you have an empty list. 
# Print your list to show that it is empty.
message = "Hi Everyone new table couldn't deliver, only space for 2 guests in Dinner Party \n"
print("\n" +message)
popped_gustlist = gustlist.pop()
print(gustlist) 
message = " Sorry for the update"
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist) 
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist) 
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist) 
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist)
message = " You are still in List \n"
print("Hi " + gustlist[0] +message)
print("Hi " + gustlist[1] +message)
del gustlist[0]
del gustlist[0]
print(gustlist)

# Excercise 3.8
# Seeing the World: Think of at least five places in the world that you would like to visit. 
# Store the locations in a list, making sure that they are NOT in alphabetical order. 
# Print your list in its original order 
# (don't worry about printing it neatly; a raw Python list output is fine). Use the "sorted()" function to print your list in alphabetical order without modifying the original list. 
# Show that your original list is still unsorted. 
# Use the "sorted()" function to print the list in reverse alphabetical order without changing the order of the original list. 
# Again, show that the original list is still unsorted. Use the "reverse()" function to change the order of the list, then print it to show the order has changed. 
# Use the "reverse()" function again to change the list back to its original order (show the output). 
# Use the "sort()" function to change your list so it's stored in alphabetical order, 
# and print the list to show the change. Use "sort()" again to store the items in reverse alphabetical order, 
# and print the list to show the change.
seeworld = ["Paris","Rome","Japan","London","Dubai"]
print(seeworld)
seeworld1 = sorted(seeworld)
print(seeworld1)
print(seeworld)
seeworld1 = sorted(seeworld, reverse= True)
print("\n")
print(seeworld1)
print(seeworld)
print("\n")
seeworld.reverse()
print(seeworld)
print("\n")

# Excercise 3.9 
# Dinner Guests: Using one of the lists from Exercises 3.4 through 3.7, 
# use the "len()" function to print a message stating how many guests you are inviting to dinner.
#gustlist = ["Binu","Sam","Lee","Jack"]
print(popped_gustlist)
message = "gusts in dinner party"
print(message)
print(len(popped_gustlist))
