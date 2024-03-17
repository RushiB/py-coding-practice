
def quick_sort(list1, l=0, r=-1):
    if r == -1: 
        r = len(list1)-1
    dbg_print = 0
    if dbg_print: print(f'quick_sort ({l},{r})')

    if l < r:
        pivot_idx = partition(list1, l,r)
        quick_sort(list1,l,pivot_idx-1)
        quick_sort(list1, pivot_idx+1, r)

def partition(list1, l, r):
    dbg_print = 0
    if dbg_print: 
        print(f'partition ({l},{r})',end=' ')
        print(list1)

    pi = l
    i = l
    pivot = list1[r]

    while i < r:
        if list1[i] < pivot:
            list1[i], list1[pi] = list1[pi], list1[i] 
            pi+= 1
        i+= 1

    list1[pi], list1[r] = list1[r], list1[pi] 
    return pi