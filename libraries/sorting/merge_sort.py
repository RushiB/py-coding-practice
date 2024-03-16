
def merge_sort(list1, start_idx, end_idx):
    dbg_print = 0
    if dbg_print: print(f'entered merge_sort({start_idx}:{end_idx})')
    
    if start_idx < end_idx:
        mid = int((start_idx + end_idx)/2)

        if end_idx - start_idx > 1:
            merge_sort(list1,start_idx, mid-1)
            merge_sort(list1,mid, end_idx)
            # OR method-2
            # merge_sort(list1,start_idx, mid)
            # merge_sort(list1,mid+1, end_idx)
        merge(list1, start_idx, mid, end_idx)
    else:
        return

def merge(list1, left_idx, mid_idx, right_idx):
    dbg_print = 0
    if dbg_print: print(f'entered merge({left_idx}:{mid_idx}:{right_idx})')
    left_arr, right_arr = [], []
    i = left_idx
    
    while (i < mid_idx) or (len(left_arr) < 1):
        left_arr.append(list1[i])
        i = i+1
    j = i
    while j <= right_idx:
        right_arr.append(list1[j])
        j = j+1

    ### same logic as above but use list slicing
    # left_arr = list1[left_idx:mid_idx]
    # if len(left_arr) == 0:
    #     if mid_idx == right_idx:
    #         right_idx = right_idx +1
    #     mid_idx = mid_idx+1
    #     left_arr = list1[left_idx:mid_idx]
        
    # right_arr = list1[mid_idx:right_idx+1]
    # temp =1

    # OR method-2
    # while ((i <= mid_idx)):
    #     left_arr.append(list1[i])
    #     i = i+1
    # j = i
    # while j <= right_idx :
    #     right_arr.append(list1[j])
    #     j = j+1


    left_ref, right_ref = 0,0
    main_ref = left_idx
    while left_ref < len(left_arr) and right_ref < len(right_arr):
        if left_arr[left_ref] < right_arr[right_ref]:
            list1[main_ref] = left_arr[left_ref]
            left_ref+= 1
            main_ref+= 1
        else:
            list1[main_ref] = right_arr[right_ref]
            right_ref+= 1
            main_ref+= 1

    while left_ref < len(left_arr):
        list1[main_ref] = left_arr[left_ref]
        left_ref+= 1
        main_ref+= 1
    
    while right_ref < len(right_arr):
        list1[main_ref] = right_arr[right_ref]
        right_ref+= 1
        main_ref+= 1
    
    return
