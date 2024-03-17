import libraries.binary_tree as binary_tree_lib
from libraries.binary_tree import binary_tree

class search_algos:
    def breadth_first_search(self, tree: binary_tree):
        
        
        pass

    def depth_first_search(self, node: binary_tree_lib.tree_node):
        if node is None:
            # print('Oh no, tree is empty!')
            return
        else:
            print(f'{node.value}')
            node.visited = True
            
            current_node = node
            if current_node.prev is not None: 
                self.depth_first_search(current_node.prev)
            if current_node.next is not None: 
                self.depth_first_search(current_node.next)
            
            

# Animated GIF for DFS expected o/p 
# https://en.wikipedia.org/wiki/Depth-first_search#/media/File:Depth-First-Search.gif
        

def test_search():
    # get a tree to search
    b_tree = binary_tree_lib.test_tree()

    algos = search_algos()
    algos.depth_first_search(b_tree.root)
    # algos.breadth_first_search(b_tree)

