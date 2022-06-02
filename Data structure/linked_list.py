class Node: 
    """
    An Object for storing  a single node of a linked list. 
    Model  two atttributes - data and the link to the next node in the last
    """
    data = None
    next_node = None 
    
    def __init__ (self, data): 
        self.data = data
    
    def __repr__ (self): 
        return "<Node data: %s>"%self.data 
    
class LinkedList:
    """
    Singly linked list
    """
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    def size(self): 
        """
        Return the number of nodes in the list 
        Take O(n) time 
        """
        current = self.head
        count = 0 
        
        while current: 
            count += 1
            current = current.next_node 
        return count
    
    def add(self, data): 
        """
        Adds new Node containing data are the end of the list 
        Takes O(1) time 
        """
        new_node = Node(data)
        new_node.next_node = self.head 
        self.head = new_node
        