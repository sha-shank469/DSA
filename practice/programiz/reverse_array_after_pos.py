
def reverse_after_m(lst, m):
    # for i in range(len(lst)):
    #     left_half = lst[:m+1]
    #     right_half = lst[m+1:]
    #     rev_lst = right_half[::-1]
    #     final_rev_list = left_half+rev_lst
    # return final_rev_list
    
    left, right = m+1, len(lst)-1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

if __name__ == "__main__":
    
    lst = [2,3,5,6,7,8]
    m = 3
    print(reverse_after_m(lst, m))
    