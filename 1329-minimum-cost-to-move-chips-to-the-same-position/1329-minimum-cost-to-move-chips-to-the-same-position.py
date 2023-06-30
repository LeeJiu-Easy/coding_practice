class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_cnt = 0
        odd_cnt = 0
        for loc in position:
            if loc % 2 == 0:
                even_cnt += 1
                continue
            odd_cnt += 1
    
        cost = 0
        if even_cnt > odd_cnt:
            for loc in position:
                if loc % 2 == 0:
                    continue
                cost +=1
        else:
            for loc in position:
                if loc % 2 == 1:
                    continue
                cost +=1

        return cost
            
                