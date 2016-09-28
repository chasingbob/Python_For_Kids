name = "John"
ages = [5, 15, 20, 25]

# For loop iterating through a list
for a in ages:
    print ("%s is now %d years old." % (name, a))
    
    
# For loop with range
startValue = 5
endValue = 10
for i in range(startValue, endValue):
    print ("i: %d" % i)
    
#TODO: Play around with the startValue and endValue and see how it affects the for loop

# Nested for loop
for i in range(1,10):
    for j in range(1,10):
        print("%d x %d = %d" % (i, j, i*j))
        

# While loop
total = 10
i = 0

while i < total:
    print ("%d < %d" % (i, total))
    i = i + 1