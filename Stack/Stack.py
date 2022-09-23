class Node:
    #function to create a node
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    #constructor of the stack
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1 

    #function to print the values of the nodes
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #function to push
    def push(self,value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1
        return True

    #function to pop
    def pop(self):
        if self.top == None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    #function to find maximum in a stack
    def find_max(self):
        temp = self.top
        max = self.top.value
        for _ in range(self.height):
            if temp.value > max:
                max = temp.value
                temp = temp.next
            else:
                temp = temp.next
        return max

#Demo Operations On Stack
my_stack = Stack(7)
my_stack.push(5)
my_stack.push(3)
my_stack.push(6)
my_stack.push(9)
print(my_stack.find_max())
#my_stack.pop()
#my_stack.print_stack()
