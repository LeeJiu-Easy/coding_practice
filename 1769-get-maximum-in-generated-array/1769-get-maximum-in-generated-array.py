class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        dp = [0, 1]
        i=1
        while len(dp) < n:
           dp.append(dp[i])
           dp.append(dp[i]+dp[i+1])
           i += 1

        return max(dp)