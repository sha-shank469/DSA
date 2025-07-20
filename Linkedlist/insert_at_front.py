class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
def insert_at_front(head, new_data):
    
    new_node = Node(new_data)
    new_node.next = head
    
    return new_node

def print_list(head):
    
    curr = head
    
    while curr is not None:
        
        print(f" {curr.data}", end="")
        curr = curr.next
        
    print()

if __name__ == "__main__":
    
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    
    print("Original Linked List:", end="")
    print_list(head)

    print("After inserting Nodes at the front:", end="")
    data = 1
    head = insert_at_front(head, data)
    
    print_list(head)