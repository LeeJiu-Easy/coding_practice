class Solution:
    def maxSum(self, nums: List[int]) -> int:
        answer = -1

        dp = [51, 71]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a_array = [int(x) for x in str(nums[i])]
                b_array = [int(x) for x in str(nums[j])]

                if max(a_array) == max(b_array):
                    answer = max(answer, nums[i] + nums[j])
        return answer