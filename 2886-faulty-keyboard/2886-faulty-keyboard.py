class Solution:
    def finalString(self, s: str) -> str:
        answer = ""
        
        for string in s:
            if string == "i":
                answer = answer[::-1]
                continue
            answer += string
        
        return answer