class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        #Counter 사용
        from collections import Counter
        
        if len(words) == 1:
            return True

        str_list = []
        for word in words:
            for string in word:
                str_list.append(string)

        word_counter = Counter(str_list)
        for frequency in word_counter.values():
            if frequency%len(words) != 0:
                return False
        return True