def twoSum(nums, target):
        for i in range(len(nums)):
            if (nums[i]<target) and (target-nums[i] in (nums[:i]+nums[i+1:])):
                s = target-nums[i]
                return [i,nums.index(s)]

nums = [3,2,4]
target = 6

print(twoSum(nums, target))