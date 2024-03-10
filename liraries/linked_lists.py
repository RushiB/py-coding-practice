class my_node:
    def __init__(self, value):
        self.value = value
        self.next =  None
        self.prev = None # used in doubly linked

class singly_linked_list:
    def __init__(self, value = 0):
        self.head = None 

    def add_node(self, value):
        if self.head == None:
            self.head = my_node(value)
            self.tail = self.head
            self.head.next = None
            print(f'added head [v:{self.head.value}]')
        else:
            new_node = my_node(value)
            self.tail.next = new_node
            self.tail = new_node
            print(f'added at tail [v:{self.tail.value}]')

    def traverse_node(self, print_end_trav_msg = False):
        if self.head == None:
            print('Oh no, linked list is empty!')
        else:
            current_node = self.head

            while current_node != None:
                print(f'{current_node.value}', end=' -> ')
                current_node = current_node.next
            print('[STOP]')

            if print_end_trav_msg:
                print('---> end of node traversal')

    def remove_node(self, value, print_list_after_remov = True):
        target_node_val = value
        current_node = self.head
        target_node_found = False
        previous_node = None

        while current_node != None:
            if current_node.value == target_node_val:
                if previous_node == None:
                    self.head = self.head.next
                else:
                    previous_node.next = current_node.next
                target_node_found = True
                print(f'removing node with val xx->{target_node_val}<-xx')
                break
            previous_node = current_node
            current_node = current_node.next
        
        if target_node_found == False:
            print(f'No node found with value {target_node_val}')
        elif print_list_after_remov:
            self.traverse_node()

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):

        new_node = my_node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(f'added head [v:{self.head.value}]')
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            print(f'added at tail [v:{self.tail.value}]')

    def traverse_nodes(self, direction = 'forward'):
        print(f'traversiong in {direction} direction')
        if direction == 'forward':
            current_node = self.head
            while current_node != None:
                print(f'{current_node.value}', end= '->')
                current_node = current_node.next
            print('[STOP]')
        else:
            current_node = self.tail
            while current_node != None:
                print(f'{current_node.value}', end= '<-')
                current_node = current_node.prev
            print('[STOP]')

    def remove_node(self, value, start_at = 'head', traverse_direction='forward', custom_msg = ''):
        target_node_found = False
        if start_at == 'head':
            current_node = self.head
        else:
            current_node = self.tail

        while current_node != None:
            if current_node.value == value:
                prev_node = current_node.prev
                next_node = current_node.next
                # removing middle node
                if prev_node != None and next_node != None:
                    prev_node.next = current_node.next
                    next_node.prev = prev_node
                
                # we are removing head node
                elif prev_node == None: 
                    self.head = next_node
                    # if more than one node, update new head's prev
                    if self.head != None:
                        self.head.prev = None
                        if self.head.next == None:
                            self.tail = self.head
                    else:
                        self.tail = None
                
                # we are removing tail node
                elif next_node == None:
                    self.tail = prev_node
                    if prev_node != None:
                        self.tail.next = None
                        if self.tail.prev == None:
                            self.head = self.tail
                    else:
                        self.tail = None

                if custom_msg == '':
                    print(f'removing node with val xx->{value}<-xx')
                else:
                    print(custom_msg)
                target_node_found = True
                break
            else:
                if start_at == 'head':
                    current_node = current_node.next
                else:
                    current_node = current_node.prev
        
        
        if target_node_found == False:
            print(f'No node found with value {value}')
        else:
            self.traverse_nodes(traverse_direction)


def test_singly_linked_list():
    linked_list1 = singly_linked_list()
    linked_list1.traverse_node(print_end_trav_msg = True)

    linked_list1.add_node(10); linked_list1.add_node(20); 
    linked_list1.add_node(30); linked_list1.add_node(40); 
    linked_list1.add_node(50); linked_list1.add_node(60); 
    linked_list1.traverse_node(print_end_trav_msg = True)

    linked_list1.remove_node(10)
    linked_list1.remove_node(40)
    linked_list1.remove_node(70)

def test_doubly_linked_list():
    linked_list1 = doubly_linked_list()

    linked_list1.traverse_nodes()
    linked_list1.add_node(10); linked_list1.add_node(20); 
    linked_list1.add_node(30); linked_list1.add_node(40); 
    linked_list1.add_node(50); linked_list1.add_node(60); 

    linked_list1.traverse_nodes(direction= 'forward')
    linked_list1.traverse_nodes(direction= 'backward')

    linked_list1.remove_node(10)
    linked_list1.remove_node(40)
    linked_list1.remove_node(70)
    linked_list1.remove_node(60, start_at= 'tail')

def test_linked_list():
    # test_singly_linked_list()
    test_doubly_linked_list()
