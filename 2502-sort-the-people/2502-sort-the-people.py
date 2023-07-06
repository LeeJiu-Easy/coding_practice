class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        answer = []
        sorted_hights = sorted(heights, reverse=True)
        
        index = []
        for height in sorted_hights:
            index.append(heights.index(height))
        
        for i in index:
            answer.append(names[i])
        return answer