

def check_palindrome(s, low, high):
    
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
        
    return True
        

def longest_palindrome(s):
    
    n = len(s)
    start = 0
    maxLen = 1
    
    for i in range(n):
        for j in range(i,n):
            
            if check_palindrome(s,i,j) and (j-i+1) > maxLen:
                start = i
                maxLen = j-i+1
    return s[start:start + maxLen]
    
    
    
    


if __name__ == "__main__":
    
    str_1 = 'babad'
    print(longest_palindrome(str_1))
    