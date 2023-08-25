class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        answer = 0
        while len(nums) >= 2:
            answer += int(f"{nums[0]}{nums[-1]}")
            nums.pop(0)
            nums.pop(-1)
        
        if nums:
            answer += nums[0]
        return answer