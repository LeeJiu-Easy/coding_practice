class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #ord 사용
        s_converted = ""

        for string in s:
            s_converted += str(ord(string)-96)

        nums = 0
        cnt = 0

        while cnt < k:
            for num in s_converted:
                nums += int(num)
            s_converted = str(nums)
            nums = 0
            cnt += 1
        return int(s_converted)