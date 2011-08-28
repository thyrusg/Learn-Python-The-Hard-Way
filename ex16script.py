from sys import argv

script, filename = argv

print "We're going to open a file"
target = open(filename, 'r')

print "Now we are going to display that file."
print target.read()




