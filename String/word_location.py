s= 'geeksforgeeks is best for geeks'
w= 'best'

try:
    res = s.split().index(w)
    return res    

except Exception as e:
    print(e)