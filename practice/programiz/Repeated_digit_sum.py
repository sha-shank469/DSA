nums = "99999999999999999999999999999999999999999999999999999999999999999999999999999999"
print("Length of number",len(nums))

result = 0
for i in range(len(nums)):
    result += int(nums[i])
    
while result >= 10:
    temp = 0
    for ch in str(result):
        temp += int(ch)
        result = temp
print("Final single digit result:", result)
