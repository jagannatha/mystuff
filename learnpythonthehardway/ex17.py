from sys import argv
from os.path import exists
script, fron_file, to_file=argv
print "copying from %s to %s" %(fron_file,to_file)
in_file=open(fron_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)
print " Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
out_file=open(to_file,'w')
out_file.write(indata)
print "alright,all done."
out_file.close()
in_file.close()
