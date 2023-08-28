class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        answer = 0
        empty = 0
        while numBottles >= 1:
            answer += numBottles
            total_empty = numBottles + empty
            numBottles = total_empty // numExchange
            empty = total_empty % numExchange

        return answer