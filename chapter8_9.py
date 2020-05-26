# Exercise 8.9 Magicians: Make a list of magician's names. Pass the list to a function called "show_magicians()", which prints the name of each magician in the list.

def show_magicians(names): 
    for name in names:       
        print(f"\n Names of Magicians in the list {name.title()} ")
m_names = ['gavin', 'savi', 'mari'] 

show_magicians(m_names)