class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        answer = 1
        cnt = 1
        for i in range(1,len(s)):
            if ord(s[i-1])+1 == ord(s[i]):
                cnt += 1
            if ord(s[i-1])+1 != ord(s[i]):
                cnt = 1
            if cnt > answer:
                answer = cnt

        return answer