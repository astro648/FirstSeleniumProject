import os
import functions
file = open('sample.txt','r')
print(file.read(5)) # prints first 5 characters in selected file
file.close() # closes file for this instance
filewrite = open('sample.txt','w')
filewrite.write("Happy new year!") # overwrites existing text with "Happy new year!" in the file
filewrite.write(" It's 2022 now") # appends It's 2022 now to Happy New Year!
filewrite.close()
file2 = open('sample.txt','r')
print(file2.read()) #prints the entire file
file2.close()
filewrite2 = open('sample.txt','a')
filewrite2.write("\nKali Linux can be used for hacking") # appends above text with this
filewrite.close()

# if os.path.exists("sample2.txt"):
#     os.remove("sample2.txt") #deletes sample2.txt
# else:
#     print("\"sample2.txt\" does not exist")
#
# if os.path.exists("folderfordeletion"):
#     os.remove("folderfordeletion")
# else:
#     print("\"folderfordeletion\" does not exist")

functions.oneplusone() #calls function from other file functions.py