class Node:
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





