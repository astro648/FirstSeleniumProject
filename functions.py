def display(text): # define a function called display() with parameter of text
    print(text)
display("Hello World") # parameter text in this case is "Hello World"

def family(*kids): # function family with parameter kids
    # the asterisk makes it so that you can pass any amount of things for the parameter "kids"
    print("Youngest child is: "+kids[2]) # in this example we don't know how many values there are
family("Joe","John","Jane") # above, kids[2] makes it so that Jane, the 3rd value, is shown

def my_function(**kid):
  print("Her last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_family(youngest="Jane"):
    print("The youngest child is: ",youngest) # using predefined parameters
my_family("Joe") # this changes Jane to Joe

def oneplusone(basevalue=1):
    doublebasevalue = basevalue*2
    print(basevalue,"+",basevalue,"=",doublebasevalue)
oneplusone()

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)