class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        dp = [[1], [1,1]]

        for i in range(2, rowIndex+1):
            new_list = [1]
            prev = 1
            for j in range(1, len(dp[i - 1])):
                new_element = prev + dp[i - 1][j]
                new_list.append(new_element)
                prev = dp[i - 1][j]
            new_list.append(1)
            dp.append(new_list)

        return dp[rowIndex]