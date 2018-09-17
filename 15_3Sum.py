class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        output = []
        for num in range(len(nums)):
            target = -nums[num]
            i,j = num + 1, len(nums) - 1
            while i < j:
                sumTwo = nums[i] + nums[j]
                if sumTwo < target:
                    i += 1
                elif sumTwo > target:
                    j-= 1
                else:
                    output.append((nums[num],nums[i],nums[j]))
                    i += 1
                    j -= 1
        return list(set(tuple(output)))
