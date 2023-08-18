class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        dp = [[1], [1,1]]

        for i in range(2, numRows):
            new_list = [1]
            prev = 1
            for j in range(1, len(dp[i - 1])):
                new_element = prev + dp[i - 1][j]
                new_list.append(new_element)
                prev = dp[i - 1][j]
            new_list.append(1)
            dp.append(new_list)
        
        return dp