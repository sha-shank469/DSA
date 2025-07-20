
def difference_two(lst):
    for i in range(len(lst)):
        if lst[i+1] - lst[i] == 2:
            return  True
        else:
            return False
 
if __name__ == "__main__":
    
    lst = [1,3,5]
    print(difference_two(lst))