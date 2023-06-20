#풀이 과정: https://url.kr/i6mwrp


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n_list = [x for x in range(1,n+1)]

        end_index = len(n_list)-1
        direction = 1
        index = 0

        while time > 0:
            if index == end_index:
                direction = -1
            elif index == 0 and direction == -1:
                direction = 1
            time -= 1
            index += direction #-1도 더한다는 개념으로
        return n_list[index]
