
def set_zeroes(matrix):
    
    
    zero_rows = set()
    zero_cols = set()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j])
            
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
    
    
    return matrix
                
    
if __name__ == "__main__":
    
    list1 = [[1,1,1], [1,0,1], [1,1,1]]
    print(set_zeroes(list1))
