class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.bstinsert(self.root, new_val)
        
    def bstinsert(self, curr, new_val):
        if new_val > curr.value:
            #traverse right
            if curr.right is not None:
                self.bstinsert(curr.right, new_val)
            else:
                curr.right = Node(new_val)
        else:
            if curr.left is not None:
                self.bstinsert(curr.left, new_val)
            else:
                curr.left = Node(new_val)
        return

    def search(self, find_val):
        return self.bstsearch(self.root, find_val)
        
    def bstsearch(self, curr, find_val):
        if find_val == curr.value:
            return True
        elif find_val > curr.value:
            #traverse right
            if curr.right is not None:
                self.bstsearch(curr.right, find_val)
            else:
                return False
        else:
            if curr.left is not None:
                self.bstsearch(curr.left, find_val)
            else:
                return False
        return False
    
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = self.preorder_print(self.root,"")
        return traversal[:-1]
    
    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        traversal = traversal + (str(start.value) + "-")
        if start.left is not None:
            traversal = self.preorder_print(start.left, traversal)
        if start.right is not None:
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

#print tree.print_tree()
# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
