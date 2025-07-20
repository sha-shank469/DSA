def correct_sentence(text):
    
    text = text[0].upper() + text[1:]
    
    if not text.endswith('.'):
        text += '.'
        
    return text
    
    


# if __name__ == "__main__":
#     print(correct_sentence("this is a test"))
    
    
text = "this is a test"
print(text[1:])