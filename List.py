#Check if anyofthe items in a list, True:

mylist = [False,True,False]
x =any(mylist)
print(x)

#set
my_set={1,1,0}
print(any(my_set))

#dictionary
my_dic={0:"a",0:"b"} 
print(any(my_dic))

#If empty, the any() will return False.
my_tuple=()
x=any(my_tuple)
print(x)


#Escape non-ascii characters:

x = ascii("My name is Ståle")
print(x)

"""
The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).

The ascii() function will replace any non-ascii characters with escape characters:

å will be replaced with \xe5.
"""


    