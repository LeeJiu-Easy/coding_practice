#리스트 길이의 1/3 이상 빈도를 갖는 숫자 찾기
#Input: nums = [3,2,3]
#Output: [3]


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        judge_dict = Counter(nums)
        answer = []
        for num, val in judge_dict.items():
            if val > len(nums)//3:
                answer.append(num)
        return answer


#배운 점: Counter()클래스는 자료형의 빈도를 판단해서 딕셔너리로 반환해 준다.
