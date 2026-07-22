class Node:  #represents one element of a doubly linked list
    def __init__(self,key):
        self.key = key #value stored in the node
        self.next = None #ref to the next node
        self.prev = None #ref to the prev node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self): #checks if the list is empty
        return self.head is None
    
    def insert(self, key): #inserts new node at the beginning of the list. Corresponds to LIST-INSERT(L, key).
        new_node = Node(key)
    
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head #the new node points to the previous first node
        self.head.prev = new_node
        self.head = new_node
    
    def search(self, key): #searches for a node containing the given key. Corresponds to LIST-SEARCH(L, Key), returns the node if found. Returns None if the key is not present.
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None
    
    def insert_after(self, new_key, searched_key): #Inserts new_key after the node containing searched_key. Corresponds to LIST-INSERT-AFTER(L, new_key, searched_key)
        searched_node = self.search(searched_key)
        if searched_node is None:
            print(
                f"Element {searched_key} was not found"
            )
            return False
        
        new_node = Node(new_key)
        new_node.prev = searched_node
        new_node.next = searched_node.next

        if searched_node.next is not None:
            searched_node.next.prev = new_node 
        else:
            self.tail = new_node

        searched_node.next = new.node
        return True
    
    def insert_before(self, new_key, searched_key): #inserts new_key before the node containing searched key. Corresponds to LIST -INSERT-BEFORE(L, new_key, searched_key)
        searched_node = self.search(searched_key)
        if searched_node is None:
            print(
                f"element {searched_key} was not found"
            )
        new_node = Node(new_key)

        new_node.next = searched.node
        new_node.prev = searched_node.prev
        if searched_node.prev is not None:
            searched_node.prev.next = new_node
            
        
