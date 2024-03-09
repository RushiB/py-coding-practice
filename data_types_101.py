# list type, tuple
# arrays, strings, bit manipulation

import array as arr

def use_arrays_strings():
    # arr1 = [1 2 3 3]
    arr1 = arr.array('i', [1, 2, 3, 4])
    print('arr1 before modifications:\t', arr1)

    arr1.append(5)
    arr1.insert(0,100)
    print('new arr1 before removals: \t', arr1)

    arr1.pop(1)
    arr1.remove(2)
    print('arr1 after modifications: \t', arr1)

    print('\n arr1 doubled: \t', arr1)
    for elem in arr1:
        print(2*elem, end= ', ')

    # strings
    str1 = str('1')
    str2 = str('2')
    new_str = str1 + str2
    print('\n new_str is : ',new_str)

    sum = 0
    for c in new_str:
        curr_num = int(c)
        sum = sum + curr_num

    print('sum of nums in new_str is : ',sum)

def use_tuple_and_list():
    tuple1 = (1,2,'a')
    # tuples are non mutable
    for item in tuple1:
        print(f'current item in tuple is: {item}')
    print(id(tuple1))
    # modification is allowed but internally new obj is created
    # thus change in address will be observed
    # same applicable for int, float etc all other non mutable type variables as well
    tuple1 = tuple1 + (3,4,5) 
    print(f'new tuple1 = {tuple1}')
    print(id(tuple1))

    list1 = [100,200,'a']
    # lists are mutable
    print(f'list1 items before update:')
    for item in list1:
        print(item)
    list1[2] = 'b'
    list1.remove(200)   # use val to remove
    temp = list1.pop(0) # use idx to remove
    print(f'popped item from list1 is: {temp}')

    list1.append('c')
    print(f'list1 item after update:')
    for item in list1:
        print(item)
    
def use_dicionary():
    dict1 = {100: 'rushi', 'type': 'dev', 200: 'two'}
    dict1[10] = 101
    dict1['city'] = 'San Diego'

    print(f'dict1 items before popping:')
    for key in dict1:
        print(f'k:{key},\t v:{dict1[key]}')

    dict1.pop(200)
    dict1.pop('type')

    print(f'dict1 items after popping:')
    print(dict1)

def count_bits_set():
    input = 23 # 0b1 0111
    temp = input
    bin_str = ''
    ones_count = 0
    while temp > 0:
        curr_bit = temp%2
        print(curr_bit)
        if curr_bit == 1:
            ones_count += 1

        bin_str = str(curr_bit) + bin_str
        temp = int(temp/2)

    print(f'0b_{bin_str}')
    print(f'1s count = {ones_count}')
    
def test():
    # use_tuple_and_list()
    # use_dicionary()
    # use_arrays_strings()
    count_bits_set()
