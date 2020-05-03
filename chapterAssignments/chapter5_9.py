# Exercise 5.9 No Users: Add an "if" test to "hello_admin.py" to make sure the list of users is not empty. If the list is empty, print the message, "We need to find some
# users!". Remove all of the usernames from your list to make sure that the correct message is printed.

user_names = []
if user_names:
    print("some users in the list")
else:
    print("We need to find some users!")