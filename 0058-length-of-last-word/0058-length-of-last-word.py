class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        target_list = s.split(' ')
        for i in range(len(target_list)):
            if len(target_list[-1]) != 0:
                return len(target_list[-1])
            target_list.pop()