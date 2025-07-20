
def highest_product(numbers):
    
    hight_prod = float('-inf')
    for i in range(len(numbers)-1):
        prod = numbers[i] * numbers[i+1]
        
        if prod > highest_product:
            hight_prod = prod
    
    return hight_prod
        


if __name__ == "__main__":
    
    numbers = [-10, -3, 1, 2, 3]
    highest_product(numbers)