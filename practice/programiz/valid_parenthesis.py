
def is_valid(s):
    
    lst = []
    for i in range(len(s)):
        
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            lst.append(s[i])
            # print(lst[-1])
        else:
            if lst and ((lst[-1] == '(' and s[i] == ')') or 
                       (lst[-1] == '{' and s[i] == '}') or
                       (lst[-1] == '[' and s[i] == ']')):
                lst.pop()
            
            else:
                return False
    
    return not lst
            
            


if __name__ == "__main__":
    
    str1 = '()[]{}'
    print(is_valid(str1))
    