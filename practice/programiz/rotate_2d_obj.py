
import math
def rotate_coordinates(coordinates, angle):
    radians = math.radians(degree)
    result = []
    for i in coordinates:
        x = i[0] * int(math.cos(radians)) - i[1] * int(math.sin(radians))
        y = i[0] * int(math.sin(radians)) + i[1] * int(math.cos(radians))
        
        result.append((round(x, 2), round(y, 2)))
        
    return result

if __name__ == "__main__":
    
    list_tuple = [(2,3)]
    degree = 90
    
    print(rotate_coordinates(list_tuple, degree))