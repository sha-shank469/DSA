
def swap_first_last(lst):
    
    # for i in range(len(lst)):
    # return lst[0], lst[len(lst)-1] == lst[len(lst)-1], lst[0]
    temp = lst[0]
    lst[0] = lst[len(lst)-1]
    lst[len(lst)-1] = temp
    
    return lst
        

if __name__ == "__main__":
    
    lst = ['apple', 'banana', 'cherry']
    print(swap_first_last(lst))