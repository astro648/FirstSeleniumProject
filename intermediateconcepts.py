print("Go to the code to see what's going on here!")
myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(myList) # prints entire list
print(myList[1]) # prints second value
print(myList[-1]) # prints last value
print(myList[-2]) # prints second to last value
print(myList[2:5]) # prints values 3-6, similar to string slicing
myList[2] = "lemon" # replaces 3rd value "cherry" in myList with "lemon"
myList.insert(2, "watermelon") # places "watermelon" in 3rd value between "banana" and "orange"
print(myList) # prints the new list
myList.append("cherry") # adds a new item called "cherry" at the end
print(myList) # prints the new list
appendList = ["carrot","celery","broccoli","spinach"] # new list to append to myList
myList.extend(appendList) # appends appendList to myList
print(myList) # prints the new list
myList.remove("watermelon") # removes "watermelon" from the list
myList.pop(3) # removes "orange" from the list
print(myList) # prints the new list
del myList[1] # deletes first value of myList
print(myList) # prints the new list
myList.sort() # sorts list alphabetically
print(myList) # prints the new list
myList.sort(reverse=True) # alphabetically but reverse
print(myList) # prints the new list
copyList = myList.copy() # copies myList to copyList
print(copyList) # prints the new list
list3 = ["a","b","c"]
list4=myList+list3
print(list4) # prints the new list
myTuple = ("abc","def","ghk") # tuple
print(myTuple)
y = list(myTuple) # converts tuple into list
myTuple = tuple(y) # converts list to tuple
fruitTuple = ("apple","banana","cherry") # when values are assigned to a tuple,
# it is called packing a tuple
(green,yellow,red) = fruitTuple # assigns values to variables - e.g. "apple" > green, "cherry" > red
print(green)
print(yellow)
print(red)
print(green, yellow, red)