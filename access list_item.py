#Access Items
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.

#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#Range of Negative Indexes
##This example returns the items from index -4 (included) to index -1 (excluded)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "jelon", "mango"]
print(thislist[-4:-1])


#Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")






