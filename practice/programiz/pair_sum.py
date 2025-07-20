
# def pairSum(arr, s):
    
#     # for i in range(len(arr)):
#     #     for j in range(len(arr)):
#     #         if arr[i] + arr[j] == s:
#     #             return arr[i], arr[j]
            
#     # return None
    
#     seen = set()
#     for num in arr:
#         complement = s - num

#         if complement in seen:
#             return complement, num
#         seen.add(num)
#     return None
        

# if __name__ == "__main__":
    
#     lst = [1,2,3,4,5]
#     sum = 5
#     print(pairSum(lst, sum))


def pairSum(arr, s):
    result = []

    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == s:
                x, y = sorted((arr[i], arr[j]))
                result.append((x, y))

    # Sort result: first by first element, then by second element
    result.sort()
    return result


if __name__ == "__main__":
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))

    pairs = pairSum(arr, target)
    for p in pairs:
        print(p[0], p[1])