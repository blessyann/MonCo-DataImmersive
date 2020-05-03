# Exercise 5.8 Hello Admin: Make a list of five or more usernames, including the name "admin". Imagine you are writing code that will print a greeting to each user
# after they log into a website. Loop through the list and print a greeting to each user. If the username is "admin", print a special greeting such as, "Hello admin, 
# would you like to see a status report?". Otherwise, print a generic greeting, "Hello Eric, thank you for logging in again." 

print("\n Hello Admin")
user_names = ['admin','eric','sam','tom','leo','faith']
for user_name in user_names:
    if user_name in 'admin':
        print(f"Hello {user_name.title()}, would you like to see a status report?\n")
    else:
        print(f"Hello {user_name.title()},thank you for logging in again.\n")

