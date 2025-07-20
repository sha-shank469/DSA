
def triangular_number(n):
    if n <= 1:
        return n
    else:
        return n + triangular_number(n-1)


if __name__ == "__main__":
    
    n = 5
    print(triangular_number(n))