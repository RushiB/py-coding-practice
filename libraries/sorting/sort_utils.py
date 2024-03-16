import libraries.sorting.merge_sort as merge_sort_lib
import libraries.sorting.quick_sort as quick_sort

def test_sort(sort_type = 'merge'):
    list1 = [9,8]
    sort_and_print(list1, sort_type)
    list1 = [9,8,7]
    sort_and_print(list1, sort_type)
    list1 = [9,8,7,6]
    sort_and_print(list1, sort_type)
    list1 = [9,8,7,6,5]
    sort_and_print(list1, sort_type)
    # return
    list1 = [9,8,7,6,5,4]
    sort_and_print(list1, sort_type)
    list1 = [8,6,4,5,7,9]
    sort_and_print(list1, sort_type)

def sort_and_print(list1, sort_type):
    if sort_type == 'merge':
        merge_sort_lib.merge_sort(list1, 0, len(list1)-1)
    
    print(f'sorted list is: {list1}', end=' \t')
    test_sorted_array(list1)

def test_sorted_array(list1): # ascending order
    passed = 1
    for i in range(1, len(list1)):
        if list1[i] > list1[i-1]:
            continue
        else:
            passed = 0
            break
    if passed: print('PASSED!')
    else: print('FAILED!')

