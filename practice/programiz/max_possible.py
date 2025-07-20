
def maximize_sum(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    return dp[-1]

if __name__ == "__main__":
    
    lst = [1,2,3,1]
    print(maximize_sum(lst))
    