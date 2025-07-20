def find_divisors(number):
    
    divisor = []
    
    for i in range(1, number+1):
        if number % i == 0:
            divisor.append(i)
        
    
    return divisor
    


if __name__ == "__main__":
    number = 12
    print(find_divisors(number))