import datetime


# Functions are used to group code together, for re-use later
# Examples of functions that takes no parameters, and returns nothing. The simplest form of a function


def print_the_time():
    print("The time is: ",datetime.datetime.now().time())
    
def print_the_date():
    print("The date is: ",datetime.datetime.now().date())
    
    
    
    

# Instead of writing out the datetime.datetime.now().time call when ever "The time is: " string is needed, you can just make a method call

print_the_time()
print_the_date()
    