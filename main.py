print("Check code for how I did this and a couple of additional comments!")
print("\n")

print("Hello World!")
print("\n")

var1 = 123
var2 = "Hello World!"
print(var2)
print(var1)
print("\n")

print("var1 : ", type(var1))
print("var2 : ", type(var2))
print("\n")

x = 1
y = 2.8
# z is a complex datatype
z = 1j
print("\n")

# datatype conversion (casting) examples
print("'x' datatype before conversion: ", type(x));
a = float(x)
print("'x' datatype after conversion: ", type(a));
print("'y' datatype before conversion: ", type(y));
b = int(y)
print("'y' datatype after conversion: ", type(b));
# complex(x) is a conversion from int to complex datatype
print("('x' datatype after conversion) 'a' datatype before conversion: ", type(a));
c = complex(x)
print("'a' datatype after conversion: ", type(c));