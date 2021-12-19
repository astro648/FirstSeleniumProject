session = "Selenium Web Driver"
print("")
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