# Exercise 5.4 Alien Colors #2: Choose a color for an alien as you did in Exercise 5.3 and write an "if-else" chain. If the alien's color is green,
# print a statement that the player just earned 5 points for shooting the alien. If the alien's color isn't green, print a statement that the player earned 10 points.
# Write one version of the program that runs the "if" block and another that runs the "else" block.

alien_colors = ['green','red','yellow']
alien_color = 'red'
if alien_color == 'green':
    print(" \n The player earned 5 points")
elif alien_color == 'red':
        print(" \n The player earned 15 points")
else:
    print("\n The player earned 10 points")