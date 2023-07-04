class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        min_num = 1
        sum_val = 0
        while sum_val <= 0:
            sum_val = min_num + 0
            for num in nums:
                sum_val += num
                print(min_num, num, sum_val)
                if sum_val <= 0:
                    min_num += 1
                    break

        return min_num