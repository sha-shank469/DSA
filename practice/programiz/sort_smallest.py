
def smallest_in_list(input):
    
    smallest = input[0]
    for i in range(1, len(input)):
        if input[i] < smallest:
            smallest = input[i]
    return smallest

def return_largest(input):
    
    largest = input[0]
    for i in range(1,len(input)):
        if input[i] > largest:
            largest = input[i]
    return largest            
        
def find_missing(small,large, input):
    
    input_set = set(input)
    for num in range(1,large):
        if num not in input_set:
            return num

if __name__ == "__main__":
    input = [3, 4, 2, 1, 5,6,8]
    
    small = smallest_in_list(input)
    large = return_largest(input)
    print(find_missing(small,large, input))