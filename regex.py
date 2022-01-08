import re  # imports regex functionality

# RegEx means Regular Expression
txt = "The rain in Taiwan"  # text to be search
x = re.search("^The.*USA$", txt)  # this line checks whether txt starts with "The"
# and ends with "USA"
if x:
    print("YES! We have a match!")
else:
    print("No match")

txt2 = "hello planet"

# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

y = re.findall("he.?o", txt2)

print(y)

# This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
