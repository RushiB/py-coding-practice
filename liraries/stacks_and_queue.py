import liraries.linked_lists as LL

class stack(LL.doubly_linked_list):
    def __init__(self):
        super().__init__()

    def push(self,value):
        super().add_node(value)

    def pop(self):
        if self.tail != None:
            val = self.tail.value
            msg = f'popping top of stack val {val}'
            super().remove_node(self.tail.value, start_at= 'tail', traverse_direction='backward', custom_msg=msg)
            return val
        else:
            print('Stack is empty! Nothing to pop!')
    

    def print_stack(self):
        super().traverse_nodes(direction= 'backward')

class queue(LL.doubly_linked_list):
    def __init__(self):
        super().__init__()

    def enque(value):
        pass
    
    def deque(value):
        pass

    

def test_stack():
    stack1 = stack()
    stack1.print_stack()

    stack1.push(10); stack1.push(20); 
    stack1.push(30); stack1.push(40); 
    stack1.print_stack(); print()
    stack1.push(50); stack1.push(60); 

    stack1.print_stack(); print()
    stack1.pop(); print()
    stack1.pop(); print()
    stack1.traverse_nodes(); print()

    stack1.pop(); print()
    stack1.traverse_nodes(); print()

    stack1.pop(); print()
    stack1.pop(); print()
    stack1.pop(); print()
    stack1.pop(); print()
    stack1.pop(); print()


def test_data_structure():
    test_stack()
    
