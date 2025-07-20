
def check_anagram(split_word, word):
    
    dict_1 = {}

    for i in split_word.lower():
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    
    for i in word.lower():
        if i in dict_1.keys():
            dict_1[i] -= 1
    
    if sum(dict_1.values()) == 0:
        return True
    else:
        return False

def find_anagram(text, word):
    
    text = text.split(' ')
    
    for split_word in text:
        if check_anagram(split_word, word):
            return split_word.lower()

    return 'Anagram not found'
    
    
    

if __name__ == "__main__":
    
    str1 = 'The quick brown fox jumps over the lazy dog'
    str2 = 'god'
    print(find_anagram(str1, str2))