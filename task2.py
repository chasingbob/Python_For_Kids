# Check the size and weight of a single parcel

# Get all the inputs
_continue = 'y' 
total_accepted = 0
total_rejected = 0
total_weight = 0

while _continue == 'y':
    print('Please supply the following values')
    length = input('length:') 
    width = input('width:')
    height = input('height:')

    print('And the weight')
    weight = input('weight in kg:')

# Validate the inputs against the rules
    errors = []
    if length > 80 or width > 80 or height > 80:
        errors.append('each dimension must be no more than 80 cm')

    if length + width + height > 200:
        errors.append('the sum of the three dimensions must be no more than 200 cm')

    if not(1 <= weight <= 10):
        errors.append('the weight of the parcel must be between one and ten kilograms inclusive')


# Output - if any errors reject and print errors or accept
    if errors:
        print('\r\nParcel Rejected')
        print('Errors:')
        for error in errors:
            print(error)
        total_rejected += 1

    else:
        print('Parcel Accepted')
        total_accepted += 1
        total_weight += weight

    _input = input('Continue? (y/n)')
    print(_input)
    _continue = _input

print('\r\nTotals:')
print('Total accepted: {}'.format(total_accepted))
print('Total rejected: {}'.format(total_rejected))
print('Total weight: {}'.format(total_weight))
