

def flash_card(question, answer):

    dict_1 = {}
    dict_1['Question'] = question
    dict_1['Answer'] = answer
    
    
    return dict_1


if __name__ == "__main__":
    
    str_1 = "What is the capital of France?"
    str_2 = "Paris"    
    print(flash_card(str_1, str_2))
