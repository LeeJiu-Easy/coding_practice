class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        answer = 0
        while len(nums) >= 2:
            answer += int(str(nums[0])+str(nums[-1]))
            del nums[0]
            del nums[-1]
        
        if nums:
            answer += nums[0]
        return answer