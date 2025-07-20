class Node:
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
def insert_after_node(head,new_data,k):
    
    new_node = Node(new_data)
    curr = head
    
    while curr is not None:
        
        if curr.data == k:
            break
        curr = curr.next
        
    if curr is None:
        print("Node not found")
        return head

    new_node.next = curr.next
    curr.next = new_node
    
    return head


def print_list(head):
    
    curr = head
    while curr is not None:
        
        print(curr.data, end= " ")
        
        curr = curr.next
    print()
    
if __name__ == "__main__":
    
    head = Node(10)
    head.next = Node(12)
    head.next.next = Node(12)
    head.next.next.next =Node(13)
    
    
    print("Original Linked list is", end=" ")
    print_list(head)
    
    key = 10
    new_data = 4
    
    head = insert_after_node(head, new_data, key)
    
    print("Linked List after insertion: ", end="")
    print_list(head)