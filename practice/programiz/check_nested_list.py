

def can_be_nested(list1, list2):
        
    max_1 = min_1 = list1[0]
    max_2 = min_2 = list2[0]

    for i in range(len(list1)):
        if list1[i] > max_1:
            max_1 = list1[i]
        if list1[i] < min_1:
            min_1 = list1[i]

    for i in range(len(list2)):
        if list2[i] > max_2:
            max_2 = list2[i]
        if list2[i] < min_2:
            min_2 = list2[i]

    if min_1 > min_2 and max_1 < max_2:
        return True
    else:
        return False
    
    # return max_1, min_1, max_2, min_2

if __name__ == "__main__":
    
    list1 = [1,2,3,4]
    list2 = [0,6]
    # print(find_max(list1, list2))
    print(can_be_nested(list1, list2))