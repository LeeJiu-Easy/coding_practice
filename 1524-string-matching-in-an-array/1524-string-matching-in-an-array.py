class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    answer.append(words[i])
                if words[j] in words[i]:
                    answer.append(words[j])
        answer = set(answer)
        return answer