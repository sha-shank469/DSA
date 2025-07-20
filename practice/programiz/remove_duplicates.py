
def find_duplicates(numbers):

    dict_1 = {}
    for i in numbers:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    
    duplicates = []
    for key in dict_1:
        if dict_1[key] > 1:
            duplicates.append(key)
    return duplicates

if __name__ == "__main__":
    
    lst = [1,2,3,2,1]
    print(find_duplicates(lst))