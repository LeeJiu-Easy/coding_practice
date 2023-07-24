class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            chunck = word.split(separator)
            for seperated_word in chunck:
                if seperated_word != "":
                    answer.append(seperated_word)
        return answer