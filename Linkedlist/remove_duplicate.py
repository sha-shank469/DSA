class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
def remove_duplicates(head):
    
    if head is None:
        return None
    
    curr = head
    
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def printList(head):
    
    curr = head
    while curr is not None:
        print(curr.data, end = " ")
        curr = curr.next
    print(" ")
    
if __name__ == "__main__":
    
    head = Node(10)
    head.next = Node(11)
    head.next.next = Node(11)
    head.next.next.next = Node(12)
    
    head = remove_duplicates(head)
    printList(head)
    