# Exercise 6.2 Favorite Numbers: Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number. 
# For even more fun, poll a few friends and get actual data for your program.

favorite_number = {'joe': 34,
                    'john': 7,
                    'lee': 25,
                    'mac': 12,
                    'cathlin': 22}
for key, value in favorite_number.items():      
    print(f"{key.title()}'s favorite number is {value}")