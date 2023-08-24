class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        common_set = nums1_set.intersection(nums2_set)

        if not common_set:
            return -1
        return min(common_set)