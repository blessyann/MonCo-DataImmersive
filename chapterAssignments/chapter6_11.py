# Exercise 6.11 Cities: Make a dictionary called "cities". Use the names of three cities as keys in your dictionary. Create a nested dictionary of information 
# about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary 
# should be something like "country", "population", and "fact". Print the name of each city and all of the information you have stored about it.

cities = {
            'Newyork city': 
            {
            'country': 'USA',
            'population': '8.623 million',        
            'fact': 'largest city'
            },
         'Chennai':
            {
             'country':'India',
             'population': '7.088 million',
             'fact': 'old name Madras'
         },
         'ocean city': {
             'country':'USA',
             'population':'6,969',
             'fact':'resort town in U.S'
         }
}
print(cities)
            
             