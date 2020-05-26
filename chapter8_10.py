# Exercise 8.10 Great Magicians: Start with a copy of your program from Exercise 8.9. Write a function called "make_great()" that modifies the list of magicians 
# by adding the phrase "the Great" to each magician's name. Call "show_magicians()" to see that the list has been modified.

m_names = ['gavin', 'savi', 'mari'] 
def make_great(names):
    for name in names:       
        print(f"\n Names of Magicians in the list {name.title()} the Great ")
        
make_great(m_names)
