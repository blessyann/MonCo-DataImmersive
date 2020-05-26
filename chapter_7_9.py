# Exercise 7.9
#   append 'pastrami' 3 times in sandwich_orders list
#   print deli is outof pastrami
#   loop through each items in sandwich_orders to check 'pastrami' in the list
#   remove item in sandwich_orders which is pastrami
#   append this sandwich_orders in finished_sandwiches
#   print finished_sandwiches and make sure 'pastrami' not present in the list


sandwich_orders = ['tuna', 'chicken','pastrami','veg','egg']
finished_sandwiches = []
for i in range(3):
    sandwich_orders.append('pastrami')
print(sandwich_orders)
print("\n  Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    print(sandwich_orders)
    sandwich_orders.remove('pastrami')
print("\n sandwich order list")
print(sandwich_orders)
for s in sandwich_orders:
    print(f"\n I made your {s.title()} sandwich")
    finished_sandwiches.append(s)   
