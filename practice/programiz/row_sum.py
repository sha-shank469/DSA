
def row_sum(matrix):
    
    sum_list = []
    
    for i in range(len(matrix)):
        sum = 0
        for j in matrix[i]:
            
            sum += j
        sum_list.append(sum)
    return sum_list
        
if __name__ == "__main__":
    
    matrix = [[1,2,3], [4,5,6],[7,8,9]]
    print(row_sum(matrix))