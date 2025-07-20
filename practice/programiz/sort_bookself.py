
def sort_books(books):
    
    sorted_books = sorted(books, key=lambda x: x['author'])
    return sorted_books
        
        
        


if __name__ == "__main__":
    
    input = [{'title':'Book1', 'author':'Author2'}, {'title':'Book2', 'author':'Author1'}]
    print(sort_books(input))
    
    