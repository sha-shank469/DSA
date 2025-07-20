
# class Solution:
#     def letterCombinations(self, digits: str):
        
#         if not digits:
#             return []
        
#         hashmap = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
#         # for i, j in hashmap.items():
#         #     print(hashmap[i])
        
#         res = []
        
#         def backtrack(idx, comb):
#             if idx == len(digits):
#                 res.append(comb[:])
#                 return  
            
#             for letter in hashmap[digits[idx]]:
#                 backtrack(idx + 1, comb + letter)

#         res = []
#         backtrack(0, "")

#         return res
            
            
# if __name__ == "__main__":
    
#     input = "23"
#     s = Solution()
#     print(s.letterCombinations(input))





dict = {1,2,3,4,5,6,6,7}
for i in dict:
    print(i )
print(type(dict))