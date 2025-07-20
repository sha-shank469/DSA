import math
def calculate_distance(point1, point2):
    
    distance = 0
    for i in range(len(point1)):
        print(i)
        distance += (point1[i] - point2[i]) ** 2
    distance = round(math.sqrt(distance), 2)
        
    return distance


if __name__ == "__main__":
    
    point1 = [1,1]
    point2 = [4,5]
    print(calculate_distance(point1, point2))