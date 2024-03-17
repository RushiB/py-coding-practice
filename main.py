import libraries.data_types_101 as types_101
import libraries.linked_lists as LL
import libraries.stacks_and_queue as staks_and_ques
import libraries.sorting.sort_utils as sort_utils
import libraries.binary_tree as btrees

''' # Note: VS code git push & Shortcut
    # -> Under commit 
    #   -> Select 'Commit & sync'
    # Shortcut added: commit: Ctrl + g + c
    # Shortcut added: sync: Ctrl + g + s
'''

global_var = 10

def hello_world():
    a = 1; b = 2; c = a + b
    print(f'hello world. c= {c}')
    global global_var
    print('global_var=',global_var)
    global_var = 2
    print('global_var=',global_var)

def try_append_sys_path_dbg():
    # note - below append is not needed, can just modules using name of parent folder
    # eg: import libraries.data_types_101 
    import sys, os
    cwd = os.getcwd()
    target_path = os.path.join(cwd, 'libraries')
    print(target_path)
    sys.path.append(target_path)

def verified_tests():
    '''
        list type, tuple
        arrays, strings, bit manipulation
    '''
    types_101.test()

    ''' 
        Single & double linked Linked lists
        stack, queue
    '''
    LL.test_linked_list()
    staks_and_ques.test_data_structure()

    sort_utils.test_sort()

btrees.test_tree()

# tree, graphs
    # binary tree - (3 types of traversals)
    # graph search:
        # DFS, BFS

# sort_utils.test_sort() #TODO: #1 radix , may be => #4 bucket sort


# recursion, dyn prog
