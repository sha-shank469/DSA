
def cumulative_sum(numbers):

    cumulative_sum = 0
    cum_sum = []
    for i in numbers:
        cumulative_sum += i
        cum_sum.append(cumulative_sum)
    return cum_sum
        
if __name__ == "__main__":
    lst = [1,2,3,4]
    print(cumulative_sum(lst))