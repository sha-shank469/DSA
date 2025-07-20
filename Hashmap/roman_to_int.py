

class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I': 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        # print(s)
        stoi = 0
        for i, val in enumerate(s):
            # print(i,val)
            # print(hashMap[val])
            
            print("legth", len(s))
            print(i, val)
            if i < len(s) -1 and hashMap[val] < hashMap[s[i+1]]:
                stoi -= hashMap[val]
                # print("stoi in if",stoi)
            else:
                stoi += hashMap[val]
                # print("stoi in else",stoi)
                
        
        return stoi


if __name__ == "__main__":
    
    str1 = "IV"
    s = Solution()
    print(s.romanToInt(str1))
