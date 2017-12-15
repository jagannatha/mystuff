i=0

numbers=[]
while  i<6:
    print "At the top i is %d"%i
    numbers.append(i)
    i=i+1
    print"Numbers now:", numbers
    print "At the bottom i is %d" %i
    J=4
    while j<10:
         print "At the top j is %d"%j
    numbers.append(j)
    i=i+1
    print"Numbers now:", numbers
    print "At the bottom j is %d" %j

    print "The Numbers:"
    for num in numbers:
        print num