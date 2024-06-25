class Solution:
    def productExceptSelf(self, nums: list[int]) -> List[int]:
        n = len(nums)
        right = [1] * n
        left = [1] * n

        for i in range(1, n):
            right[i] = right[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            left[i] = left[i+1] * nums[i+1]
        
        
        answer = [1] *n
        for i in range(n):
            answer[i] = right[i] * left[i]
        return answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        pre=1
        post=1
        for i in range(n):
            answer[i]*=pre
            pre = pre*nums[i]
            answer[n-i-1]*=post
            post=post*nums[n-1-i]
        return answer