
def add_matrix_values(lst):
    
    total = lst[0][0]
    
    op = ' ' # Default operator in case first number is not operator
    
    element = [elem for row in lst for elem in row][1:]
    # print(element)

    # for row in lst:
    #     for ele in row:
    #         print(type(ele))


    for ele in element:
        if type(ele) == str:
            op = ele
        else:
            if op == '+':
                total += ele
            if op == '-':
                total -= ele
            if op == '*':
                total *=  ele
            if op == '/':
                total /= ele
    
    return total

if __name__ == "__main__":
    
    lst = [[1, '+', 2], ['-', 3], ['*', 2]]
    print(add_matrix_values(lst))