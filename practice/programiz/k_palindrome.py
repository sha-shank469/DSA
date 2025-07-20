def is_k_palindrome(s, k):

    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        print(i)
        dp[i][i] = 1
        for j in range(i+1, n):
            print(j)
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    lps_length = dp[0][n-1]
    min_deletions = n - lps_length

    return min_deletions <= k


if __name__ == "__main__":
    
    str_1 = 'abcdeba'
    k = 2
    print(is_k_palindrome(str_1, k))


# s = 'abcdeba'
# n = len(s)

# for i in range(n-1, -1, -1):
#     print(s[i])