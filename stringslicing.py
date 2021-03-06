session = "Selenium Web Driver"
print("To get a context and explanation of what is happening, go to the code.")
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
startagetext = "The age that I started using computers is {} and at the time of creating this my age is {}"
startage = "5"
currentage = "12"
print(startagetext.format(startage,currentage))
# basically with .format(), you add values to the original string
# example:
# arbitrarystring = "value goes here: {}"
# value = 123
# print(arbritrarystring.format(value))
# or you can add multiple values by using commas as demonstrated outside of the comments
age = "my age is \"12\""
print(age)
# use \ before characters like " to make it show
value = "asdf23"
alnum = value.isalnum()
alnumstr = str(alnum)
print("Is \""+value+"\" alphanumeric? : "+alnumstr)
# .isalnum() checks if the value is alphanumeric
number = "123"
alpha = number.isalpha()
alphastr = str(alpha)
print("Is \""+number+"\" completely made of alphabet? : "+alphastr)
# .isalpha() checks whether the value inputted is completely alphabet
alpha2 = value.isalpha()
alphastr2 = str(alpha)
print("Is \""+value+"\" completely made of alphabet? : "+alphastr2)
# likewise, this works with strings that are alphanumeric
num = number.isnumeric()
numstr = str(num)
print("Is \""+number+"\" completely made of numbers? : "+numstr)
# .isnumeric() is .isalpha() but number
check = 2>3
boolcheck = bool(check)
strboolcheck = str(boolcheck)
print("2>3? : "+strboolcheck)
# Checks if a certain equation is true and outputs the bool