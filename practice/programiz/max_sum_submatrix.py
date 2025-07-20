def max_sum_submatrix(matrix):
    
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    
    for left in range(cols):
        print("left",left)
        
        temp = [0] * rows
        for right in range(left, cols):
            print("right", right)
            for i in range(rows):
                temp[i] += matrix[i][right]
            
            curr_sum = temp[0]
            curr_max = temp[0]
            for i in range(1, rows):
                curr_sum = max(temp[i], curr_sum + temp[i])
                curr_max = max(curr_max, curr_sum)
            
            max_sum = max(max_sum, curr_max)
            
    return max_sum

if __name__ == "__main__":
    
    matrix = [[1,-2,-1, -4, -20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
    
    print(max_sum_submatrix(matrix))