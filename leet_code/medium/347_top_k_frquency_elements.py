#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        sorted_num = Counter(nums).most_common()
        answer = []
        i = 0
        for (num, _) in sorted_num:
            if i == k:
                break
            answer.append(num)
            i += 1
        return answer
