
def second_largest(numbers):
    numbers_sort = sorted(numbers)
    # print(numbers_sort)
    
    return numbers_sort[-2]

if __name__ == "__main__":
    
    lst = [2,3,4,5]
    print(second_largest(lst))

    