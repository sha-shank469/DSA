
def sum_of_evens(matrix):

    even_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            if matrix[i][j] % 2 == 0:
                even_sum += matrix[i][j]
            else:
                continue
    return even_sum

if __name__ == "__main__":
    
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    
    print(sum_of_evens(matrix))