from sys import argv
script , filename= argv
txt=open(filename) #It actually makes something called a "file object." 

print "Here is your file %r:" %filename
print txt.read()

print "Type the filename again:"
file_again=raw_input("----->")

txt_again=open(file_again)
print txt_again.read()
