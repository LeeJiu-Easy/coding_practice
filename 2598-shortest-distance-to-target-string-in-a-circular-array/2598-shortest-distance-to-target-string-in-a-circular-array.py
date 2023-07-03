class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        if target not in words:
            return -1

        left = 0
        right = 0
        n = len(words)

        for _ in range(len(words)):
            if words[(startIndex+right)%n] == target:
                break
            elif words[(startIndex-left)%n] == target:
                break
            right += 1
            left += 1

        return min(left, right)