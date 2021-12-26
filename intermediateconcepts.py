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