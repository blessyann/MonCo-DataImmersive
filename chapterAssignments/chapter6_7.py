# Exercise 6.7 People: Start with the program that you wrote for Exercise 6.1. Make two dictionaries representing different people, and store all three dictionaries 
# in a list called "people". Loop through your list of people. As you loop through the list, print everything you know about each person.

person = {'first_name': 'sue',
          'last_name': 'tom',
          'age': 25,
          'city': 'silver spring'}
person_1 ={'first_name': 'yee',
          'last_name': 'man',
          'age': 28,
          'city': 'baltimore'}
person_2 = {'first_name': 'matt',
          'last_name': 'levi',
          'age': 45,
          'city': 'silver spring'}

people = []
people.append(person)    
print(people)
print("\n")
people.append(person_1)    
print(people)
print("\n")
people.append(person_2)    
print(people)
print("\n")

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + ", of " + city + ", is " + age + " years old.")
    print("\n")


    
   
    
