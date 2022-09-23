class Node:
    #Node creation for Binary Search Tree
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    #Constructor for a Binary Search Treeclass Node:
    #Node creation for Binary Search Tree
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    #Constructor for a Binary Search Tree
    def __init__ (self):
        self.root = None

    #Function to insert a Node 
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
              
    #Function to check whether it contains the value          
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else :
                return True
        return False

    #Function to find minimum node value in BST
    def min_value_node(self, current_node):
        while current_node.left :
            current_node = current_node.left
        return current_node.value
    
    #Function to find maximum node value in BST
    def max_value_node(self, current_node):
        while current_node.right:
            current_node = current_node.right
        return current_node.value

    def bfs(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

    def dfs_preorder(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

    def dfs_postorder(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result

    def dfs_inorder(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

#Demo Operations
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(18))
print(my_tree.min_value_node(my_tree.root))
print(my_tree.min_value_node(my_tree.root.right))
print(my_tree.max_value_node(my_tree.root))
print(my_tree.bfs())
print(my_tree.dfs_preorder())
print(my_tree.dfs_postorder())
print(my_tree.dfs_inorder())
