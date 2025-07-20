

def word_order(words):
    
    dict_1 = {}

    for i in words:
        
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    return dict_1


if __name__ == "__main__":

    lst = ['apple','banana','apple', 'cherry','banana', 'cherry']
    print(word_order(lst))