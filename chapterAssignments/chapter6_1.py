# Exercise 6.1 Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and city in which they live. 
# You should have keys such as "first_name", "last_name", "age", and "city". Print each piece of information stored in your dictionary.

person = {'first_name': 'sue',
          'last_name': 'tom',
          'age': 25,
          'city': 'silver spring'}
for key, value in person.items():      
    print(f"{key.title()} of the person is {value}")