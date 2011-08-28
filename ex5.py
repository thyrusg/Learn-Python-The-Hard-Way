name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

lbs2kilo = weight / 2.2 #Divide the lbs by 2.2 to get the kilo amount
inches2centimeters = height * 2.54 #Multiply the height in inches by 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "This is Zed's weight in kilos", lbs2kilo
print "This is Zed's height in centimeters", inches2centimeters 

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)
