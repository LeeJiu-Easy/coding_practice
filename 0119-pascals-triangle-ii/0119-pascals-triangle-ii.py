class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        dp = [1]

        for i in range(1, rowIndex+1):
            new_list = []
            for j in range(i+1):
                if j == 0 or j == i:
                    new_list.append(1)
                else:
                    new_list.append(dp[j-1] + dp[j])
            dp = new_list
        return dp