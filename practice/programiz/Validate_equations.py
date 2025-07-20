def true_equations(equations):
    result = []
    for eq in equations:
        left, right = eq.split('=')
        # print(left, right)
        if eval(left) == eval(right):
            result.append(eq)
    
    return result

equations = ['2+2=4', '3*3=6', '1+1=3', '5/5=1']
print(true_equations(equations))