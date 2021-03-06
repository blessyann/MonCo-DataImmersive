# Exercise 6.3 A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
# Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and
# then print its meaning on the second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {'int': 'integer',
            'char': 'character',
            'parameter': 'variable',
            'function': 'task',
            'print': 'output'}
print("\n programming words ad its meaning:!\n")
for key, value in glossary.items():      
    print(f"The programming word '{key.title()}' means  \t {value.title()}\n")

# Excercise 6.4 Now that you know how to loop through a dictionary, clean up the code from Exercise 6.3 by replacing your series of print statements with a loop 
# that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary_new = {'str': 'string', 
                'append': 'add', 
                'loop': 'iterate',
                'syntax': 'format',
                'for':'loop'}   
glossary.update(glossary_new) 
print("\t The new updated dictionary is\n")
for key, value in glossary.items():      
    print(f"The programming word '{key.title()}' means  \t {value.title()}\n")


