from libraries.data_types_101 import my_node

class tree_node(my_node):
    def __init__(self, value):
        super().__init__(value)
        self.visited = False

class binary_tree():
    def __init__(self) -> None:
        self.root = None

    def add_node(self, val):
        new_node = tree_node(val)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.value >= val:
                    if current_node.prev == None:
                        current_node.prev = new_node
                        break
                    else:
                        current_node = current_node.prev
                else:
                    if current_node.next == None:
                        current_node.next = new_node
                        break
                    else:
                        current_node = current_node.next


    def traverse_tree(self):
        if self.root is None:
            print('Oh no, tree is empty!')
            return
        else:
            current_node = self.root
            # in-order traversal
            if current_node.prev is not None: 
                self.print_sub_tree(current_node.prev)
            
            self.print_sub_tree(current_node)
            
            if current_node.next is not None: 
                self.print_sub_tree(current_node.next)


    def print_sub_tree(self, current_node:tree_node):
        if current_node is None:
            return
        else:
            if current_node is not None and not current_node.visited:
                if (current_node.prev is not None) and (not current_node.prev.visited):
                    self.print_sub_tree(current_node.prev)

                print(current_node.value)
                current_node.visited = True

                if (current_node.next is not None) and (not current_node.next.visited):
                    self.print_sub_tree(current_node.next)

                



def test_tree():
    test_set1, test_set2 = 0, 1
    if test_set1:
        b_tree = binary_tree()
        b_tree.add_node(5)
        b_tree.add_node(12)
        b_tree.add_node(1)
        b_tree.traverse_tree()
    
    if test_set2:
        b_tree = binary_tree()
        b_tree.add_node(50)
        b_tree.add_node(27)
        b_tree.add_node(61)
        b_tree.add_node(45)
        b_tree.add_node(19)
        b_tree.add_node(72)
        b_tree.add_node(56)
        b_tree.add_node(58)
        b_tree.add_node(52)
        b_tree.add_node(47)
        b_tree.traverse_tree()
