
def multiply_digit(n):
    
    multiply = 1
    for i in str(n):
        multiply *= int(i)
    return multiply 
    

if __name__ == "__main__":
    
    n = 123
    print(multiply_digit(n))