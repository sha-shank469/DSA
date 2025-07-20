

def diagonally_dominant(matrix):
    
    sum_diagonal = 0
    sum_non_diag = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum_diagonal += abs(matrix[i][j])
            else:
                sum_non_diag += abs(matrix[i][j])
    
    if sum_diagonal > sum_non_diag:
        return True
    else:
        return False 
    
    
if __name__ == "__main__":
    
    matrix = [[3,-2], [1,3]]
    print(diagonally_dominant(matrix))