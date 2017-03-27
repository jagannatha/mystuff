from sys import argv
script , filename = argv
print "We are going to erse %s:" % filename
print " If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file......"
target=open(filename,'w')#opens the file in write mode

print "Truncating the file. Goodbye!"
target.truncate()

print "Now am going to ask you for the three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print"I'm going to write these to the file."
target.write(line1)#writes the first line  
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close() #once all the write will finishes it will closes
