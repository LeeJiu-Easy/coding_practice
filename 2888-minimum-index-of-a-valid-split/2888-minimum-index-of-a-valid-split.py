class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #1. 가장 빈도가 높은 숫자를 찾는다
        #2. 빈도*2 가 길이보다 크고 1개의 도미넌트가 나오도록 리스트를 잘라본다
        #3. 두 리스트가 모두 조건에 충족할 때까지 반복   
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

                    
            