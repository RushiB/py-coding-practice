import libraries.binary_tree as binary_tree_lib
import queue

class search_algos:
    def breadth_first_search(self, node: binary_tree_lib.tree_node):
        if node is None:
            return
        else:
            bfs_q = queue.SimpleQueue()
            bfs_q.put(node)

            while bfs_q.empty() is not True:
                nw_node = bfs_q.get()
                self.print_node(nw_node)

                if nw_node.prev != None and nw_node.prev.visited is False:
                    nw_node.prev.visited = True
                    bfs_q.put(nw_node.prev)
                if nw_node.next != None and nw_node.next.visited is False:
                    nw_node.next.visited = True
                    bfs_q.put(nw_node.next)
                

    def print_node(self, node: binary_tree_lib.tree_node):
        # node.visited = True
        print(f'{node.value}')

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


def test_search():
    # get a tree to search
    b_tree = binary_tree_lib.test_tree(traverse_tree=False)

    algos = search_algos()

    # Animated GIF for DFS expected o/p 
    # https://en.wikipedia.org/wiki/Depth-first_search#/media/File:Depth-First-Search.gif
    if 0:
        algos.depth_first_search(b_tree.root)
    
    if 1:
        algos.breadth_first_search(b_tree.root)

