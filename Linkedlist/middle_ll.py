class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
def getLength(head):
    length = 0
    
    while head:
        length += 1
        head = head.next
    
    return length
    
    
def getMiddle(head):
    
    length = getLength(head)
    
    mid_index = length // 2
    
    while mid_index:
        head = head.next
        mid_index -= 1
    
    return head.data
    
    
    
if __name__ == "__main__":
    
    head = Node(10)
    head.next = Node(11)
    head.next.next = Node(12)
    head.next.next.next = Node(13)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    
    print(getMiddle(head))
