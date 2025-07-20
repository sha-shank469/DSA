
def split_into_chunks(lst, size):
    
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i+size])
    
    return result

if __name__ == "__main__":
    
    input_list = [1, 2, 3, 4, 5,6]
    chunk_size = 2
    print(split_into_chunks(input_list, chunk_size))