
def last_letter(n):
    
    last_num = []
    for i in n:
        last_num.append(str(i)[::-1][0])
        
    return last_num
         
    

if __name__ == "__main__":
    n = [123, 456, 789]    
    print(last_letter(n))