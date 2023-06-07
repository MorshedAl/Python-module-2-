#change/replace list item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# change a range of item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#replace চেয়ে বেশি insert করলে, সব ইনক্লুড হয়ে,এডজাস্ট হবে।
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#কম insert করলেও, যত replace হওয়ার কথা, রিপ্লেস হয়ে এডজাস্ট হয়ে যাবে।
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# insert(): To insert without replace.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 








