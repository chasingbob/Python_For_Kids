

def print_appropriate_message(age, name):
    if (age < 10):
        print('{} is in primary school'.format(name))
    elif (age >= 10 and age < 20):
        print('{} is most likely in high school'.format(name))
    else:
        print('{} is too old for school'.format(name))


age = 17
name = "John"


print_appropriate_message(age, name)
print_appropriate_message(8, 'Angie')
print_appropriate_message(88, 'Grandpa Jack')

    
