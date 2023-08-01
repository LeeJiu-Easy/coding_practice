class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
    
        nums_dict = defaultdict(int)
        
        for key, value in nums1:
            nums_dict[key] = value

        for key, value in nums2:
            if nums_dict[key]:
                nums_dict[key] += value
            else:
                nums_dict[key] = value      
        
        answer = []
        index_list = sorted(nums_dict.keys())
        
        for i in index_list:
            answer.append([i, nums_dict[i]])
        
        return answer
