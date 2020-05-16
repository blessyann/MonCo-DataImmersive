# Exercise 6.8 Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the 
# owner's name. Store these dictionaries in a list called "pets". Next, loop through your list and as you do, print everything you know about each pet.

cat = {'petname': 'jimmy',
        'owner': 'tom'}
dog = {'petname': 'doggy',
        'owner': 'jack'}
parrot = {'petname': 'mari',
        'owner': 'matt'}
pets = []
pets.append(cat)
pets.append(dog)
pets.append(parrot)
print(pets)
for p in pets:
    name = p['petname'].title() 
    owner = p['owner'].title()
    print(name + ", is  " + owner +"'s pet")
    print("\n")