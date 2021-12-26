mySet = {"webbtelescope", 123, True} # Sets are made
# similarly to lists but they can be any types of values and are unordered
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021,
  "color": ["Twister Orange", "Yellow Peel", "Lucid Red Pearl", "Velocity Blue", "Ford Performance Blue", "Absolute Black", "Antimatter Blue", "Iconic Silver Metallic", "Carbonized Gray Metallic", "Fighter Jet Gray", "Race Red", "Oxford White"]
}
print(thisdict)
x = 1324865823465
if x > 0:
    print(x, " is a positive number")
elif x == 0:
    print(x," = 0")
else:
    print(x," is a negative number")
a = 330
b = 330
print("A") if a > b else print(a,"=",b) if a == b else print("B")
a = 2
b = 10
print(a) if a < b else print(b)
if b > a:
  pass
#while b > a:
#    if b == 5:
#        continue
#    print(b)
#    b = b-1
#i = 0
#while i < 6:
#  i += 1
#  if i == 3:
#    continue
#  print(i)
for z in mySet: # this prints mySet
    print(z)
for x in range(6):
  print(x)
else:
  print("Finally finished!")

dict1 = {1: "Bitcoin", 2: "Ethereum"}
for key, value in dict1.items():
    print(f"Key {key} has value {value}")