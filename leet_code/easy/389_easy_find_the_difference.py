#문제: 문자열 2쌍의 차이점 찾기
#Input: s = "abcd", t = "abcde"
#Output: "e"

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        s_judge = Counter(s)
        t_judge = Counter(t)
        answer = ""
        check_multi = set()

        for letter in t:
            if letter in check_multi:
                continue
            if t_judge[letter] != s_judge[letter]:
                answer += letter
                check_multi.add(letter) 
        return answer
