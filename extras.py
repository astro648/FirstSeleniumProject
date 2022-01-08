import mymodule as mm  # mm replaces mymodule when needed

from mymodule import person1  # imports library person1

mm.myfunc()  # instead of writing mymodule.myfunc() we write mm.myfunc()
x = mm.x  # uses the x value from mm
print(x)  # it is still 200, referencing changing the global variable

print(person1["name"])  # prints value "name" from library person1
