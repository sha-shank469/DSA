
def circular_shift(lst):
    
    # return [lst[-1]] + lst [:-1]
    num = 1 % len(lst)
    return lst[-num:] + lst[:-num]
        

if __name__ == "__main__":
    lst = [1,2,3,4,5]
    print(circular_shift(lst))