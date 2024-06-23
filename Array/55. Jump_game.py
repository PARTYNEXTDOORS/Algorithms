class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = 0
        for i in range(len(nums) - 1):
            a = max(a - 1, nums[i])
            if a == 0:
                return False
        return True
