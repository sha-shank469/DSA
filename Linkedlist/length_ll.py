class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
    
def count_node(head):
        
    count = 0
    
    curr = head
    
    while curr is not None:
        count += 1
        curr = curr.next
    
    return count

if __name__ == "__main__":
    
    head = Node(1)
    
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(4)
    
    print("Count of Node is", count_node(head))
    