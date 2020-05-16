# Exercise 6.6 Polling: Use the code from the "favorite_languages.py" lesson example.
# Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet 
# taken the poll, print a message inviting them to take the poll.

favorite_languages = {'jen':['python','ruby'],
                       'sarah':['c'],
                       'edward':['ruby','go'],
                       'phil':['python','haskell']}
poll_list = ['jen','sarah','edward','phil','jim','lee','sam']
for i in poll_list:
        if i in favorite_languages.keys():
            print(f"\n {i} Thankyou for taking the poll")
        else:
            print(f"\n {i} Please join the poll")
    
