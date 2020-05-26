# Exercise 8.5 Cities: Write function called "describe_city()" that accepts the name of a city and its country. The function should print a simple sentence,
#  such as "Reykjavik is in Iceland." Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not 
# in the default country.

def describe_city(city_name, country='U.S.A'):
    print(f"\n {city_name.title()} is in :- {country}")
    
    
describe_city('newyork city')
describe_city('Silver spring')
describe_city('chennai','India')