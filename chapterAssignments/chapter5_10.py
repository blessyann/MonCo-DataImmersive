# exercise 5.10 Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username:

current_users = ['a','b','c','d','e','f']
new_users = ['h','i','b','d','f','k']
for new_user in new_users:
    if new_user in current_users:
        print(f"\n {new_user}  will need to enter a new username.")
    else:
        print(f"\n {new_user} username is available")