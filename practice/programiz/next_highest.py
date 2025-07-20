
"""
convert digit to list
start from the end, and find the first digit i such that digits[i] < digits[i+1]
if no such digit found - number already the highest permutation, so return it
Otherwise, find the smallest digit to the right of digits[i] that's larger than digits[i].
Swap them.
Reverse the part of the list after i.
"""

### IMPORTANT QUES

def next_higher_number(num):

    digits = list(str(num))
    n = len(digits)
    
    for i in range(n-2, -1, -1):
        if digits[i] < digits[i+1]:
            break
        else:
            return num
    # print(digits[i])
    
    for j in range(n-1, i , -1):
        if digits[j] > digits[i]:
            break
    
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])

    return int("".join(digits))

if __name__ == "__main__":
    
    n = 123
    print(next_higher_number(n))