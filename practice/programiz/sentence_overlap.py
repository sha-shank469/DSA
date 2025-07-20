def check_overlap(sentence):

    sentence_split = sentence.split(' ')
    for i in range(len(sentence_split)):
        if sentence_split[i][-1] == sentence_split[i+1][0]:
            return True
        else:
            return False
        
if __name__ == "__main__":
    
    string = 'She eats strawberries'
    
    print(check_overlap(string))