# Exercise 6.5 Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be "nile" : "egypt" .
# Use a loop to print a sentence about each river, such as "The Nile runs through Egypt."
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

Rivers = {'nile':'egypt',
          'amazon':'brazil',
          'ganga':'india',
          'hudson':'america'}
for key, value in Rivers.items():
    print(f"The {key.title()} runs through {value.title()}\n")
print("The rivers in the list are \n")
for key in Rivers.keys():
    print(f"{key}\t")
print(Rivers.keys())
print("\n  The countries are \n") 
for value in Rivers.values():
    print(f"{value}\n")

