def longest_zero_sequence(binary_string):
    
    max_len = 0
    current_len = 0
    for i in binary_string:
        if i == '0':
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        
        else:
            current_len = 0
    return max_len

str = '10100100010001'
print(longest_zero_sequence(str))