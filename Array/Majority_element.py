class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        my_hash = {}
        for i in nums:
            if i in my_hash:
                my_hash[i] += 1
            else:
                my_hash[i] = 1
        return max(my_hash, key=lambda k: my_hash[k])


class SolutionPython:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n // 2]
