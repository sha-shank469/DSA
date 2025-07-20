
def min_diff_pair(lst):
    lst.sort()
    min_diff = float('inf')
    pair = (None, None)
    
    for i in range(1,len(lst)):
        diff = lst[i] - lst[i-1]
        if diff < min_diff:
            min_diff = diff
            pair = (lst[i-1], lst[i])
    return pair

if __name__ == "__main__":
    
    lst = [1,5,3,19,18,25]
    print(min_diff_pair(lst))
    