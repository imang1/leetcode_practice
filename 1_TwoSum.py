class Solution(object):
    def twoSum(self, nums, target):
        lookUp = {}
        i = 0
        while i < len(nums):
            lookUp.update({nums[i]:i})
            i += 1
        i = 0
        while i < len(nums):
            complement = target - nums[i]
            if complement in lookUp and lookUp.get(complement) != i:
                return [i,lookUp.get(complement) ]
            i += 1
