class Solution:
    def balancedStringSplit(self, s: str) -> int:
        #R개수 세기
        #L개수 세기
        r_counter = 0
        l_counter = 0
        answer = 0
    
        for string in s:
            if string == 'R':
                r_counter +=1
            if string == 'L':
                l_counter += 1
            if r_counter == l_counter:
                answer += 1
                r_counter = 0
                l_counter = 0
        
        return answer