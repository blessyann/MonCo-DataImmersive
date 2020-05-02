#Exercise 3.1
names = ["John", "Tom", "Jim", "Eric","Erin", "Leo"]
print(names)
names.sort()
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

#Exercise 3.2
message= "God Bless You "
print(message + names[0])
print(message  + names[1])
print(message  + names[2])
print(message  + names[3])
print(message  + names[4])
print(message  + names[5])


#Exercise 3.3
foods = ["Indian","Chinese","Mexican","American"]
print("I would like to eat " + foods[0] + " breakfast") 
print("I would like to eat " + foods[1] + " Lunch") 
print("I would like to eat " + foods[3] + " Dinner") 

#Excercise 3.4
gustlist = ["Binu","Sam","Lee","Jack"]
message = " I would like to invite you to our Dinner party"
print("Hi " + gustlist[0] + message ) 
print("Hi " + gustlist[1] + message ) 
print("Hi " + gustlist[3] + message ) 

#Excercise 3.5
message = "Hi Everyone Lee couln't attend the Dinner Party"
gustlist[2] = "Eric"
print(gustlist)
message = " Dont forget the Dinner party "
print("Hi " + gustlist[0] + message ) 
print("Hi " + gustlist[1] + message ) 
print("Hi " + gustlist[2] + message ) 
print("Hi " + gustlist[3] + message ) 

#Excercise 3.6
message = "\n Hi Everyone More tables avilable in Dinner Party \n"
print(message)
gustlist.insert (0, "Jim")
gustlist.insert (2, "sue")
print(gustlist)
gustlist.append("Liz")
print(gustlist)
message = " Dont forget the Dinner party on Monday"
print("\nHi " + gustlist[0] + message ) 
print("Hi " + gustlist[1] + message ) 
print("Hi " + gustlist[2] + message ) 
print("Hi " + gustlist[3] + message )
print("Hi " + gustlist[4] + message )
print("Hi " + gustlist[5] + message )
print("Hi " + gustlist[6] + message )

#Excercise 3.7
message = "Hi Everyone new table couldn't deliver, only space for 2 guests in Dinner Party \n"
print("\n" +message)
popped_gustlist = gustlist.pop()
print(gustlist) 
message = " Sorry for the update"
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist) 
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist) 
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist) 
print("\n Hi " + popped_gustlist + message)
popped_gustlist = gustlist.pop()
print(gustlist)
message = " You are still in List \n"
print("Hi " + gustlist[0] +message)
print("Hi " + gustlist[1] +message)
del gustlist[0]
del gustlist[0]
print(gustlist)

#Excercise 3.8
seeworld = ["Paris","Rome","Japan","London","Dubai"]
print(seeworld)
seeworld1 = sorted(seeworld)
print(seeworld1)
print(seeworld)
seeworld1 = sorted(seeworld, reverse= True)
print("\n")
print(seeworld1)
print(seeworld)
print("\n")
seeworld.reverse()
print(seeworld)
print("\n")

#Excercise 3.9 
#gustlist = ["Binu","Sam","Lee","Jack"]
print(popped_gustlist)
message = "gusts in dinner party"
print(message)
print(len(popped_gustlist))













