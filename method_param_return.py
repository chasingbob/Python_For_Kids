from random import randint


# Simple function taking 1 argument
def print_message(name):
    print("Hello %s" % name)
    
# Taking Multiple arguments
def print_name_age(name, age):
    print("Hello %s you are %d years old" % (name, age))
    
# Function returning something
def give_me_random_number_between_1_and_10():
    return randint(0,9)
    
# Functions can also take parameters and return something
def add_random_number(my_number):
    return my_number + give_me_random_number_between_1_and_10()
    



    
    

print_message("Samuel")
print_name_age("Samuel", 17)
random_number = give_me_random_number_between_1_and_10()
print("Your random number is: %d" % random_number)

print("========================")

number = 7
print("My number is: %d" % number)
my_new_number = add_random_number(number)
print("My new number is: %d" % my_new_number)

# Where things get realy interesting is where you can pass a function call to a function as a parameters
print("========================")
print(add_random_number(give_me_random_number_between_1_and_10()))