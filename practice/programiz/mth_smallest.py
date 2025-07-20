

def find_mth_smallest(lst,m):
    
    new_lst = []
    
    for i in range(len(lst)):
        for j in lst[i]:
            new_lst.append(j)
    sorted_list = sorted(new_lst)
    
    return sorted_list[m-1]

if __name__ == "__main__":
    
    list_1 = [[1,3,5], [2,4,6], [0,7,8],[9,10,11]]
    m = 5
    
    print(find_mth_smallest(list_1, m))
    
    
    