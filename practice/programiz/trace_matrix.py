def calculate_matrix_trace(matrix):
    
    # it should be a square matrix
    row = len(matrix)
    cols = len(matrix[0])
    sum = 0
    
    if row == cols:
        for i in range(len(matrix)):
            sum += matrix[i][i]
    
    return sum
                            
            
            
if __name__ == "__main__":
    
    lst = [[1,2,3], [4,5,6], [7,8,9]]
    print(calculate_matrix_trace(lst))