import mymodule as mm  # mm replaces mymodule when needed
import datetime as dt  # dt replaces datetime
from mymodule import person1  # imports library person1

mm.myfunc()  # instead of writing mymodule.myfunc() we write mm.myfunc()
x = mm.x  # uses the x value from mm
print(x)  # it is still 200, referencing changing the global variable

print(person1["name"])  # prints value "name" from library person1

x = dt.datetime.now()
print(x)  # prints current date and time
print(x.year)  # only prints current year
print(x.strftime("%A"))  # prints current day's name (e.g. Friday)
# if %a (lowercase) is used, only Fri from above example will print

