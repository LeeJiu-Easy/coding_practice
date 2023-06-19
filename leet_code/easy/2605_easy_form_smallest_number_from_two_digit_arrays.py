#Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.
#Input: nums1 = [4,1,3], nums2 = [5,7]
#Output: 15

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        intersection_set = set(nums1).intersection(set(nums2))
        
        answer = 0
        if intersection_set:
            answer = min(list(intersection_set))
        else:
            nums1_min= min(nums1)
            nums2_min = min(nums2)
            if nums1_min < nums2_min:
                answer = int(str(nums1_min)+str(nums2_min))
            else:
                answer = int(str(nums2_min)+str(nums1_min))
        return answer
