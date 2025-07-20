class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

def insert_before_key(head, new_data, key):

    new_node = Node(new_data)
    
    if head is None:
        return None
    
    if head.data == key:
        new_node.next = head
        return new_node
    
    head.next = insert_before_key(head.next, key, new_data)
    
    return head

def print_list(head):
    
    curr = head
    while curr is not None:
        print(curr.data, end = " ")
        curr = curr.next
    
    print()

if __name__ == "__main__":
    
    head = Node(10)
    head.next = Node(11)
    head.next.next = Node(12)
    head.next.next.next = Node(13)
    
    new_data = 6
    key = 12
    
    head = insert_before_key(head, new_data, key)
    
    print_list(head)