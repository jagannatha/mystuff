x = " There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s AND those who %s . " %(binary,do_not)
print x
print y
print " I said: %r ."% x
print "I also said: '%s' ." %y
hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"
print joke_evaluation % hilarious
w = "This is the left side of........."
e = "a String with a rigth side ......"
print w + e


#----------------NOTES---------------
#1 What is the difference between %r and %s?
# Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.
