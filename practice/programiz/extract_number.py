
def extract_numbers(s):
    res = ""
    for i in s:
        if i.isdigit():
            res += i
    return res if res else None


if __name__ == "__main__":
    
    str1 = 'hello123world456'
    print(extract_numbers(str1))