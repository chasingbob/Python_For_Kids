# Check the size and weight of a single parcel

def calculate_cost(weight):
    if weight > 1 and weight <= 5:
        return 10
    elif weight > 5:
        over_weight_grams = (weight - 10) * 1000
        total = over_weight_grams / 100
        return (float(total) * 0.1) + 10
	

# Get all the inputs
_continue = 'y' 
total_accepted = 0
total_rejected = 0
total_weight = 0
total_price = 0

while _continue == 'y':
    print('Please supply the following values')
    length = int(input('length:'))
    width = int(input('width:'))
    height = int(input('height:'))

    print('And the weight')
    weight = int(input('weight in kg:'))

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
        parcel_price = calculate_cost(weight)
        total_price += parcel_price
        print('Parcel price: {:2,.2f}'.format(parcel_price))

    _input = input('Continue? (y/n)')
    print(_input)
    _continue = _input

print('\r\nTotals:')
print('Total accepted: {}'.format(total_accepted))
print('Total rejected: {}'.format(total_rejected))
print('Total weight: {}'.format(total_weight))
print('Total price: {:2,.2f}'.format(total_price))
