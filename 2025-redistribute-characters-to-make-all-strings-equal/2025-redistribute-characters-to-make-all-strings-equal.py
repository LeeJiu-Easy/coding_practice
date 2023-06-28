class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        #Counter 사용
        from collections import Counter
        
        if len(words) == 1:
            return True
        
        str_counter = Counter()
        for word in words:
            str_counter += Counter(word)
    
        for frequency in str_counter.values():
            if frequency%len(words) != 0:
                return False
        return True