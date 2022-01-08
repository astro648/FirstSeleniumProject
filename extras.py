import mymodule as mm  # mm replaces mymodule when needed

mm.myfunc()  # instead of writing mymodule.myfunc() we write mm.myfunc()
x = mm.x     # uses the x value from mm
print(x)     # it is still 200, referencing changing the global variable
