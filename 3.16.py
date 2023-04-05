numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
temp_largest = None
print('before', temp_largest)

for number in numbers:
    if temp_largest is None:
        temp_largest = number
    elif number > temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'The largest value is {temp_largest}')