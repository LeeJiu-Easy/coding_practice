class Solution:
    def countDigits(self, num: int) -> int:
        if num <= 9:
            return 1

        answer = 0
        for num_str in str(num):
            if num % int(num_str) == 0:
                answer += 1
        return answer