class Solution:
    def jump(self, nums: list[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums) - 1):
            a = max(a, nums[i])
            # TODO не работает
        return b
    # ошибка!!!
