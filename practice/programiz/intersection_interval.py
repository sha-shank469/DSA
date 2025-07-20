
def intersection_interval(interval1, interval2):
    
    start = max(interval1[0], interval2[0])
    print(start)
    end = min(interval1[1], interval2[1])
    print(end)
    
    if start < end:
        
        return [start, end]

    else:
        return []
                
        


if __name__ == "__main__":
    
    lst1 = [1, 5]
    lst2 = [3, 7]
    print(intersection_interval(lst1, lst2))