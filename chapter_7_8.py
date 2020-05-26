# exercise 7.8 & 7.9
# 2 lists sandwich_orders : stors the names of sandwich
#         finished_sandwiches : maded sandwich
# loop through sandwich_orders
# print each sandwich name with a message "I made your sandwich name"
# append that sandwith name to finished_sandwiches  
# print  finished_sandwiches

sandwich_orders = ['tuna', 'chicken','pastrami','veg','egg']
finished_sandwiches = []
for s in sandwich_orders:
    print(f"\n I made your {s.title()} sandwich")
    finished_sandwiches.append(s)    
print("\nList of made Sandwich ###\n ")
print(finished_sandwiches)




    