def repeated_char(str):
    
    dict_1 = {}
    for i in str:
        if i in dict_1.keys():
            return i
        else:
            dict_1[i] = 1
    return None


if __name__ == "__main__":
    
    str = "hello"
    
    print(repeated_char(str))
    
    