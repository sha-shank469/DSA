
def group_anagrams(strs):

    dict_of_groups = {}
    lst = []
    for i in strs:
        dict1 = {}
        for j in i:
            if j not in dict1:
                dict1[j] = 1
            else:
                dict1[j] += 1
                
        key = tuple(sorted(dict1.items()))
        if key not in dict_of_groups:
            dict_of_groups[key] = []
        dict_of_groups[key].append(i)
    
    for group in dict_of_groups.values():
        group.sort()
        lst.append(group)
    
    return lst
                
if __name__ == "__main__":
    
    lst = ['eat','tea','tan','ate','nat','bat']
    print(group_anagrams(lst))