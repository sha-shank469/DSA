
def max_sublist_sum(nums):
    
    res = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum = curr_sum + nums[j]

            res = max(res, curr_sum)
    return res
    

if __name__ == "__main__":
    
    lst = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sublist_sum(lst))