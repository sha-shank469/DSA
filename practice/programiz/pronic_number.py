def is_pronic(n):
    x = 0
    while x * (x+1) <= n:
        if x * (x + 1) == n:
            return True
        
        x += 1
    return False

print(is_pronic(6))   
print(is_pronic(12))  
print(is_pronic(7))


"""A pronic number is a number that is the product of two consecutive integers.
It can be written as:

n = x * (x + 1)

"""