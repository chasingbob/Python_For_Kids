# repitition

# At the simplest level you can use repitition to iterate through a list of items
# With each iteration you pick the next item in the list
fruits = ['banana', 'apple', 'peach']

# For loop iterating through a list
for fruit in fruits:
    print('Hi you {}'.format(fruit))
    
    
# For loop with range
startValue = 5
endValue = 10
for i in range(startValue, endValue):
    print ("i: %d" % i)
    
# Nested for loop
# This is a loop within a loop - play with different values
for i in range(1,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i, j, i*j))
        

# While loop
# The while loop will continue to iterate while a condition is met
count = 0
total = 0

# As long as 
while count < 10:
    print ('Count: {} Total'.format(count, total))
    count += 1        # increment count by one 
    total += count    # same as total = total + count
print('I am outside of the scope of the above while loop')
# NB that Python uses indentation to group code together - the above print line will only get executed once the while loop finished


# Condition within a loop (repitition)
# You can have any amount of logic within a while loop e.g below I've implemented a method te check if a number is odd, 
# and I've added some condition logic inside the loop to check

def is_even(x):
    if x % 2 == 0:
        return True
    return False
count = 0
while count < 10:
    if is_even(count):
        print('EVEN')
    else:
        print('ODD')
    count += 1