# Python program showing simple implementation of the bubble sort algorithm and some examples

# Ref: CL Education 2.2.2

def bubble_sort(values):
# Crude implementation of the bubble sort algorithm

    sorted = values[:]
    length = len(sorted)
    for i in range(0,length):
        swapped = False
        for element in range(0, length-i-1):
            if sorted[element] > sorted[element + 1]:
                hold = sorted[element + 1]
                sorted[element + 1] = sorted[element]
                sorted[element] = hold
                swapped = True
        if not swapped: break

    return sorted


values = [17, 19, 12, 3, 23, 21]
sorted = bubble_sort(values)
print('Values: {}'.format(values))
print('Sorted: {}'.format(sorted))

values = [15.4, 15.1, 15.7, 15.6, 15.2]
sorted = bubble_sort(values)
print('Float values: {}'.format(values))
print('Sorted: {}'.format(sorted))

# As an exercise, replace the outside for loop and replace with a while loop