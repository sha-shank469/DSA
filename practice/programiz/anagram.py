
def is_anagram_substring(s1, s2):

    dict_1 = {}
    for i in s1:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    print(dict_1)
    
    for i in s2:
        if i in dict_1.keys():
            dict_1[i] -= 1
    
    if sum(dict_1.values()) == 0:
        return True
    else:
        return False    
    

if __name__ == "__main__":
    
    str1 = 'abc'
    str2 = 'cba'
    print(is_anagram_substring(str1, str2))