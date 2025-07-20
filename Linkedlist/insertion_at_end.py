class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def insertAtEnd(head, new_data):
    
    curr = head
    new_node = Node(new_data)
    
    if curr is None:
        return new_node
    
    while curr.next:
        curr = curr.next
    
    curr.next = new_node
    
    return head
    

def print_list(head):
    
    curr = head
    while curr is not None:
        print(curr.data, end= " ")
    
        curr = curr.next
    

if __name__ == "__main__":
    
    head = Node(10)
    head.next = Node(101)
    head.next.next = Node(102)
    
    print(print_list(head))
    
    
    head = insertAtEnd(head, 2)
    print("\nAfter inserting 1 at the end: ", end="")
    print_list(head)