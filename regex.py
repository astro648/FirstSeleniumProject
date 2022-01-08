import re # imports regex functionality
# RegEx means Regular Expression
txt = "The rain in Taiwan" # text to be search
x = re.search("^The.*USA$", txt) # this line checks whether txt starts with "The"
# and ends with "USA"
if x:
  print("YES! We have a match!")
else:
  print("No match")