def divisor(n):

    divisor = []
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
            
    return divisor


def check_deficient(divisor_res, n):
    
    result = 0
    for i in divisor_res:
        result += i
        
    if result < n:
        return True
    else:
        return False

if __name__ == "__main__":
    
    n = 12
    divisor_res = divisor(n)
    print(check_deficient(divisor_res , n))