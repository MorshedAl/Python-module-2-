#list method 

#Add an element to list:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


#append(), add two list
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)


#clear()
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)


#copy()
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

#count()
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

#extend()
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)


#Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

#index()
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#duplicate হলে, প্রথমটির index return করে।
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

#insert(idx,value)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#pop()
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#Return the removed element:
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

#remove(x)
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#duplicate হলে, প্রথমটি রিমোভ।
fruits = ['apple', 'banana', 'cherry','banana']
fruits.remove("banana")
print(fruits)


#reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sort(),alphabetically 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# descending order sorting 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)



# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)


#Sort a list of dictionaries based on the "year" value of the dictionaries:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)



#Sort the list by the length of the values and reversed:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)





