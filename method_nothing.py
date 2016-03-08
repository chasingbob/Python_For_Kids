import datetime


# Functions are used to group code together, for re-use later
# Examples of functions that takes no parameters, and returns nothing. The simplest form of a function


def print_the_time():
    print("The time is: ",datetime.datetime.now().time())
    
def print_the_date():
    print("The date is: ",datetime.datetime.now().date())
    
# Method can call other methods
def print_date_and_time():
    print("Date & Time")
    print_the_date
    print_the_time
    
    
    
    
    

# Instead of writing out the datetime.datetime.now().time call when ever "The time is: " string is needed, you can just make a method call to a function

print_the_time()
print_the_date()
print("==============")
print_date_and_time()
    