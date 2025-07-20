
def ginortS(s):
    return "".join(sorted(s , key = lambda c:(
        c.isdigit() == False,
        c.isupper(),
        c.isdigit() and int (c) % 2 == 0,
        c.lower(),
        c
    )))
    

if __name__ == "__main__":
    
    str1 = "Sorting1234"
    print(ginortS(str1))
    
    