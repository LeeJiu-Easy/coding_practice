class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        visit = set(nums1)
        answer = set()
        for num in nums2:
            if num in visit:
                answer.add(num)
        
        visit.update(nums2)
        for num in nums3:
            if num in visit:
                answer.add(num)
      
        return answer