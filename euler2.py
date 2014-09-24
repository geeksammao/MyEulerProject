def create_fibonacci():
    nums = [1,2]
    i = 0
    num = 0
    while num < 4000000:
        num = nums[i] + nums[i+1]
        nums.append(num)
        i += 1
    return nums
    
def sum(nums):
    result = 0
    for i in nums:
        if i % 2 == 0:
            result += i
        
    return result
    
print sum(create_fibonacci())                
        