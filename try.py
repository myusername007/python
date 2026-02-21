
nums = [2,7,11,15]
target = 9
   
def sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]
        
        seen[num] = i

print(sum(nums,target))
