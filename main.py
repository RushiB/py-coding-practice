import sys, os
libs_path = os.path.join(os.getcwd(), 'libraries')
sys.path.append(libs_path)

import liraries.data_types_101 as types_101
import liraries.linked_lists as LL
import liraries.stacks_and_queue as staks_and_ques


def hello_world():
    a = 1; b = 2; c = a + b
    print(f'hello world. c= {c}')

def append_sys_path_dbg():
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

# Linked list, stack, queue
# LL.test_linked_list()
staks_and_ques.test_data_structure()

# sorting and searching
# tree, graphs
# recursion, dyn prog