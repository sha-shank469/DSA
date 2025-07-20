
def complete_square(matrix):
    
    row = len(matrix)
    cols = len(matrix[0])
    
    # for i in range(row):
    #     if len(matrix[i]) != row:
    #         return False
    #     else:
    #         return True
    
    for i in range(row):
        current_len = len(matrix[i])
        if current_len < row:
            matrix[i].extend([0]*(row - current_len))
    
    return matrix
            
            
        
if __name__ == "__main__":
    
    matrix = [[1,2], [3]]
    print(complete_square(matrix))