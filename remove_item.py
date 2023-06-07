#remove list item:
#remove(),pop(),del
#remove():
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#renove specified index
#pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#remove last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#The 'del' keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
