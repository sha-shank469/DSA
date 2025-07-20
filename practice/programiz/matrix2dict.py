
def matrix_to_dict(matrix):
    matrix_dict = {}
    
    for i in range(len(matrix)):
        
        matrix_dict[i] = matrix[i]
        
    return matrix_dict

if __name__ == "__main__":
    
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix_to_dict(matrix))