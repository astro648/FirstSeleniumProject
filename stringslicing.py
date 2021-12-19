session = "Selenium Web Driver"
print("To get a context of what is happening, go to the code.")
# [x:y] <-- Array
# x is starting value, y is ending value
# array always starts at 0
# so instead of counting 1,2,3,4,5,6
# you would count 0,1,2,3,4,5
print(session[:8])
# if you want to start from 0, instead of writing [0:y] just write [:y]
print(session[0:])
# in this situation lets call z the end value
# if you want to start from the end, instead of writing [x:z] you just write [x:]
print(session.upper())
# if you want the whole thing to go to uppercase
# in this example we want the string session to go to uppercase
# just write variable.upper()
print(session.lower())
# lowercase: same thing as uppercase but it's lower
print(session.strip())
# to remove all the extra spaces from string, use .strip()
print(session.replace("e","3"))
# in this example, we can use "x" as the original character
# and "y" as the replacement
# to replace a character, use:
# .replace("x","y"
print(session.split(" "))
# in this example, "b" can be the character we want to split based on
# also, the string "a" with the content "abababa" will be split
# .split("b") changes abababa to ['a','a','a','a']
string1 = "Hello"
string2 = "World"
print(string1+string2)
# in this example string1 ("Hello")
# is concatenated with string2 ("World")
# to create "HelloWorld"
# by using + in between the values
print(string1+" "+string2)
# same example but with a space
print(string1+" "+"World")
# you can also concatenate strings and directly written values