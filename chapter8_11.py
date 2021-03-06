# Exercise 8_11 Unchanged Magicians: Start with your work from Exercise 8.10. Call the function "make_great()" with a copy of the list of magicians' names. 
# Because the original list will be unchanged, return the new list and store it in a separate list. Call "show_magicians()" with each list to show that you have one 
# list of the original names and one list with "the Great" added to each magician's name.

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    return great_magicians

magicians = ['gavin', 'savi', 'mari']
print("\nOriginal magicians:")
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians)
show_magicians(great_magicians)