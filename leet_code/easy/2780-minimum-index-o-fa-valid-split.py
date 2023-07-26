#An element x of an integer array arr of length m is dominant if freq(x) * 2 > m, where freq(x) is the number of occurrences of x in arr. Note that this definition implies that arr can have at most one dominant element.

#Input: nums = [1,2,2,2]
#Output: 2
#Explanation: We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 

class Solution:
    def minimumIndex(self, nums: List[int]) -> int: 
        from collections import Counter
        
        split_counter = Counter()

        num_counter = Counter(nums)
        most_common_elements = num_counter.most_common()[0][0]
        
        split_left_len = 0        
        split_right_len = len(nums)
        
        answer = -1

        for i in range(len(nums)):
            split_counter[nums[i]] += 1
            num_counter[nums[i]] -= 1

            split_left_len += 1
            split_right_len -= 1
            
            if nums[i] == most_common_elements:
                if split_counter[nums[i]] * 2 > split_left_len and num_counter[nums[i]] * 2 > split_right_len:
                    answer = i
                    break
        return answer