
# def move_zeroes_to_end(arr):
    
#     n = len(arr)
#     temp = [0]*n
#     j = 0 
    
#     for i in range(n):
#         if arr[i] != '0':
#             temp[j] = arr[i]
#             j+=1
    
#     while j < n:
#         temp[j] = '0'
#         j += 1
    
#     return temp
        
# if __name__ == "__main__":
    
#     n = 1020304050
#     lst = []
#     for i in str(n):
#         lst.append(i)
#     result = move_zeroes_to_end(lst)
#     print(result)



# def move_zeroes_to_end(n):
    
#     n = str(n)
    
#     temp = [0]*n
#     j = 0 
    
#     for i in range(n):
#         if arr[i] != '0':
#             temp[j] = arr[i]
#             j+=1
    
#     while j < n:
#         temp[j] = '0'
#         j += 1
    
#     return temp

def move_zeroes_to_end(n):
    cnt=1
    str1=""
    for i in str(n):
        if i=='0':
            cnt+=1
        else:
            str1+=i
    return str1+"0"*cnt
            
        
if __name__ == "__main__":
    
    n = 1020304050
    result = move_zeroes_to_end(n)
    print(result)