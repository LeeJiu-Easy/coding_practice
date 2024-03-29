class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10**4+1 for x in range(len(nums))]
        dp[0] = 0
        
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                next_idx = i+j
                if next_idx < len(nums):
                    dp[next_idx] = min(dp[next_idx], dp[i] + 1)
        return dp[-1]