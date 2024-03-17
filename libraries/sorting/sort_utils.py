import libraries.sorting.merge_sort as merge_sort_lib
import libraries.sorting.quick_sort as quick_sort

def test_sort(sort_type = 'merge'):
    # sort_type = 'pivot'
    test_set1, test_set2, test_set3 = 1,0,0
    if test_set1:
        list1 = [9,8]
        sort_and_print(list1, sort_type)
        list1 = [9,8,7]
        sort_and_print(list1, sort_type)
        # return
    
    if test_set2:
        list1 = [9,8,7,6]
        sort_and_print(list1, sort_type)
        list1 = [9,8,7,6,5]
        sort_and_print(list1, sort_type)
        # return
    
    if test_set3:
        list1 = [9,8,7,6,5,4]
        sort_and_print(list1, sort_type)
        list1 = [8,6,4,5,7,9]
        sort_and_print(list1, sort_type)
        list1 = [1,2,3,4,5,6]
        sort_and_print(list1, sort_type)
        list1 = [5,4,6,1,3,2]
        sort_and_print(list1, sort_type)
        list1 = [7,5,5,2,1,6,9,8,4,6,3,5]
        sort_and_print(list1, sort_type)

def sort_and_print(list1, sort_type):
    if sort_type == 'merge':
        merge_sort_lib.merge_sort(list1, 0, len(list1)-1)
    elif sort_type == 'pivot':
        quick_sort.quick_sort(list1)
    
    print(f'sorted list is: {list1}', end=' \t')
    test_sorted_array(list1)

def test_sorted_array(list1): # ascending order
    passed = 1
    for i in range(1, len(list1)):
        if list1[i] >= list1[i-1]:
            # check all preceding elements are lower as well
            j = i
            while j >= 1:
                if list1[i] < list1[i-1]:
                    passed = 0
                    break
                j = j-1
        else:
            passed = 0
            break
    if passed: print('PASSED!')
    else: print('FAILED!')

