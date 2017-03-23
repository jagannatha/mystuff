#Variables cannot start with integers
# -*- coding: utf-8 -*- at the top if you use non-ASCII characters and get an encoding error
my_name = 'Jagannatha.M.V'
my_age = 26
my_height = 154 #inches
my_weight = 180 #lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'Black' 
print"Let's talk about %s" % my_name
print"He's %d inches tall" % my_height
print" He's %d pounds heavy"% my_weight
print"actually that's not too heavy"
print"He's got %s eyes and %s hair" % (my_eyes,my_hair)
print"His teeth are usually %s depending on the coffe" % my_teeth
print"If I add %d,%d,and %d I get %d" %(my_height,my_weight,my_age,my_age+my_weight+my_height)
#----------------NOTES---------------
#1 What does %s, %r, and %d do again?
# they are "formatters." They tell Python to take the variable on the right and put it in to replace the %s with its value,
#2 How can I round a floating point number?
# You can use the round() function like this: round(1.7333).
#3 I get this error TypeError: 'str' object is not callable.
# You probably forgot the % between the string and the list of variables.
