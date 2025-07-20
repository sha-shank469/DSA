def findUnique(arr, n) :
    #write your code here 
    dict1 = {}
    for i in arr:
        if i not in dict1:
            
            dict1[i] = 1
        else:
            dict1[i] += 1
    print("Dict1",dict1)
    for i in dict1:
        if dict1[i] == 1:
            return i

if __name__ == "__main__":
    
    
    # arr = [2, 3, 1, 6, 3, 6, 2]
    arr = [1,1,5]
    
    n = 7
    print(findUnique(arr,n))
