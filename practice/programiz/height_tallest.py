
def tallest_building(lst):
    
    tallest = lst[0]
    for i in lst:
        if i > tallest:
            tallest = i
    return tallest
    

if __name__ == "__main__":
    
    lst = [100, 200, 150, 300]
    print(tallest_building(lst))