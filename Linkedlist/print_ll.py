class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
def printList(head):
    
    curr = head
    
    while curr is not None:
        
        print(curr.data, end= " ")
        
        curr = curr.next


if __name__ == "__main__":
    
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    
    
    printList(head)