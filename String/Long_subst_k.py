test_str = "abcaaaacbbaa"

print("The original String is:" + str(test_str))

k = 'a'

cnts = 0
res = 0


for idx in range(len(test_str)):
    
    if test_str[idx] == k:
        cnts += 1
        
    else:
        cnts = 0
        
    res = max(res, cnts)
    

print("The Longest Substring Length is" + str(res))