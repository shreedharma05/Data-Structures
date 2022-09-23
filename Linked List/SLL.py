#Function To Create A Node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

#Constructor Of The LL
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #To Print The LL
    def print_list(self) :
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #To Append A New Value In The LL
    def append(self,value):
        new_node = Node(value)
        #if the ll is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    #To Pop From The LL
    def pop(self):
        #if the ll is empty
        if self.length == 0 :
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        #if the ll is empty after deduction
        if self.length == 0 :
            self.head = None
            self.tail = None
        return temp.value

    #To Prepend A New Value In The LL
    def prepend(self,value):
        new_node = Node(value)
        #if the ll is empty
        if self.length == 0 :
            new_node = self.head
            new_node = self.tail
        else :
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
    
    #To Pop First From The LL
    def pop_first(self):
        #if the ll is empty
        if self.length == 0 :
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        #if the ll is empty after deduction
        if self.length == 0 :
            self.tail = None
        return temp

    #To Get A Value From The LL
    def get(self,index) :
        if index < 0 or index >= self.length :
            return None
        temp = self.head
        for _ in range(index) :
            temp = temp.next
        return temp

    #To Set A New Value For A Node
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    #To Insert A Value In The LL
    def insert(self,index,value):
        if index < 0 or index > self.length :
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.length :
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    #To Remove A Value In The LL
    def remove(self,index):
        if index < 0 or index > self.length :
            return None
        if index == 0 :
            return self.pop_first()
        if index == self.length :
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    #To Reverse A LL
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



            

#Test 
my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.prepend(1)
my_linked_list.reverse()
my_linked_list.print_list()


