class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_dict = {}
        for i,j in enumerate(nums):
            r = target - j
            if r in ans_dict:
                return [ans_dict[r], i]
            ans_dict[j] = i
        