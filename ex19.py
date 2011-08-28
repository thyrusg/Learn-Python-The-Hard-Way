#makes a function called cheeese_and_crackers with arguments for how much cheese, and how many boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count #prints how much cheese using %d
    print "You have %d boxes of crackers!" % boxes_of_crackers #prints how many boxes of crackers using %d
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
#you give the function cheese_and_crackers, its values directly by putting them in ()'s. This makes the arguments equal to the numbers in the ().
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

""" you create the same arguments outside of the script as variables and assign them values. 
    The function can use the values from the variables since they have the same names as the
    arguments in the script"""
print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#calls the function defined above but it uses the values from the variables that we created above. 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Give the function numbers directly like above, except in the form of an equation
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#pass arguments to the function by adding the variables we created above with actual numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
