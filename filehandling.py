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
filewrite2 = open('sample.txt','w')
filewrite2.write("Kali Linux can be used for hacking") # completely overwrites the above text with this