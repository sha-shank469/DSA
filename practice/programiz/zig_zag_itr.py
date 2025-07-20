# Important Question

def zig_zag_itr(list1, list2):
    
    result_lst = []
    len1, len2 = len(list1), len(list2)
    
    max_len = max(len1, len2)
    
    for i in range(max_len):
        
        if i < len1:
            result_lst.append(list1[i])
        
        if i < len2:
            result_lst.append(list2[i])
            
    print(result_lst)
    return result_lst        
    
if __name__ == "__main__":
    lst1 = [1,2]
    lst2 = [3,4,5,6]
    zig_zag_itr(lst1, lst2)