class Node:

    #Function to create a node
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    #Constructor of the Queue
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    #To print the Queue
    def print_queue(self):
        temp = self.first
        while (temp):
            print(temp.value)
            temp = temp.next

    #To Enqueue
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            new_node = self.last
        self.length += 1

    #To Dequeue
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if(self.length == 1):
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


#Demo Operations
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.dequeue()
my_queue.print_queue()


        
