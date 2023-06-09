
# Find the Difference
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 생애 첫 Counter 클래스 사용.
        # Counter는 자료형의 빈도를 파악해서 딕셔너리로 반환
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
