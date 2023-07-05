class Solution:
    def maxScore(self, s: str) -> int:
        #첫번째 자리부터 잘라서 0개수 세기
        #오른쪽으로 1개수 세기
        #두번째 자리로 잘라서 0개수 세기
        #오른쪽으로 1개수 세기
        from collections import Counter


        left = ""
        right = ""


        answer = []
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            left_cnt = Counter(left)
            right_cnt = Counter(right)
            answer.append(left_cnt['0'] + right_cnt['1'])

        return max(answer)