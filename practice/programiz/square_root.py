

def square_root(n):
    
    result = n
    while result >= 2:
        result = round(result ** 0.5, 2)

    return result
        
    


if __name__ == "__main__":
    
    n = 256
    print(square_root(n))