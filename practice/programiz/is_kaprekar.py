

def is_kaprekar(n):
    
    sq = str(n * n)
    d = len(str(n))

    # Split the square string into two parts
    right = int(sq[-d:]) if sq[-d:] else 0
    left = int(sq[:-d]) if sq[:-d] else 0

    # Check Kaprekar condition
    return (left + right) == n
    
    
    
    
if __name__ == "__main__":
    
    n = 45
    print(is_kaprekar(n))