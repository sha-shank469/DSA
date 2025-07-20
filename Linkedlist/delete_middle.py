class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
def deleteMid(head):
    
    if head is None:
        return None
    
    if head.next is None:
        return None
    
    prev = None
    slow_ptr = head
    fast_ptr = head
    
    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        
        prev = slow_ptr
        
        slow_ptr = slow_ptr.next
        
    prev.next = slow_ptr.next
    
    return head
        

def printList(head):
    
    curr = head
    while curr is not None:
        print(curr.data, end = " ")
        curr = curr.next
    
    print("None")
    

if __name__ == "__main__":
    
    head = Node(10)
    head.next = Node(11)
    head.next.next = Node(12)
    head.next.next.next = Node(13)
    head.next.next.next.next = Node(14)
    head.next.next.next.next.next = Node(15)
    
    
    print("Original Linked List: ",end = " ")
    printList(head)

    head = deleteMid(head)
    
    print("Linked List after deleting the middle node: ", end="")
    printList(head)