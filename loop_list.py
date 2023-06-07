#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



#Use the range() and len() functions to create a suitable iterable.
#Print all item by index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#while loop:,
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#looping using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


