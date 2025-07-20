
def spiral_order(matrix):
    
    m = len(matrix)
    n = len(matrix[0])

    res = []
    top, bottom, left, right = 0, m-1, 0, n-1

    while top <= bottom and left <= right:

        # left to right
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1

        # top to bottom
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1

        # right to left
        if top <= bottom:
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        # bottom to top
        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1

    return ''.join(str(i) for i in res)
            
            
        
if __name__ == "__main__":
    
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    
    print(spiral_order(matrix))