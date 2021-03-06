import mymodule as mm  # mm replaces mymodule when needed
import datetime as dt  # dt replaces datetime
from mymodule import person1  # imports library person1
import json  # imports json functionality

mm.myfunc()  # instead of writing mymodule.myfunc() we write mm.myfunc()
x = mm.x  # uses the x value from mm
print(x)  # it is still 200, referencing changing the global variable

print(person1["name"])  # prints value "name" from library person1

x = dt.datetime.now()
print(x)  # prints current date and time
print(x.year)  # only prints current year
print(x.strftime("%A"))  # prints current day's name (e.g. Friday)
# if %a (lowercase) is used, only Fri from above example will print
# (shortened version)

y = dt.datetime(2022, 1, 7, 17)  # custom date with Yr, Mo, Day, Hr
print(y)  # prints custom date
print(y.strftime("%B"))  # prints current month's name using the custom date
# lowercase B will print the shortened version as well
print(y.strftime("%w"))  # this will print weekday number from 0 to 6
print(y.strftime("%W"))  # this will print month number from 01 to 12
print(y.strftime("%d"))  # this will print day number of the month

print(x.strftime("%H"))  # this will print the hour of the day in 24h number format

# JSON is a format for storing and exchanging data
# This is an example
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
x2 = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.loads(x)
# the result is a Python dictionary:
print(y["name"], "\'s age is ", y["age"])

# py --> json
y2 = json.dumps(x2)
print(y2) # this prints the JSON in raw form
