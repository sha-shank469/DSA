def check_prime(n):
    
    if n <= 1:
        return False
    for i in range(2,n):
        # print(i)
        if n % i == 0:
            return False
    return True

def check_composite(n):
    if n <= 1:
        return False
    
    if check_prime(n):
        return False
    else:
        return True

if __name__ == "__main__":
    n = 4
    print(check_composite(n))