class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
def insert_pos(head, pos, data):
    
    if pos < 1:
        return None
    
    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        
        return new_node
    
    curr = head
    
    for _ in range(1, pos-1):
        
        if curr == None:
            break
        curr = curr.next
        
    if curr is None:
        return head
    
    new_node = Node(data)
    new_node.next = curr.next
    curr.next = new_node
    
    return head
    
    
def print_list(head):
    curr = head
    
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
        
    print()
    
    
if __name__ == "__main__":
    
    head = Node(10)
    head.next = Node(11)
    head.next.next = Node(12)
    
    data = 14
    pos = 3
    
    head = insert_pos(head, pos, data)
    
    print_list(head)