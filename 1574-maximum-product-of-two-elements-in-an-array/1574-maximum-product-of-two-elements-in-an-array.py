class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #이중 포문
        
        if len(nums) == 2:
            return (nums[0]-1)*(nums[1]-1)
        
        i = 0
        j = 0

        nums_sorted = sorted(nums, reverse=True)

        for idx in range(len(nums)):

            if nums[idx] == nums_sorted[0]:
                i = idx
            elif nums[idx] == nums_sorted[1]:
                j = idx
        if nums_sorted[0] == nums_sorted[1]:
            return (nums[i]-1) * (nums[i]-1)
        else:
            return (nums[i]-1) * (nums[j]-1)