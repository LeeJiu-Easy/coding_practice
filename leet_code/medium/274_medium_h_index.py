#https://url.kr/eynzku

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #최소 인용횟수 이상의 논문을 발표했다면 결과로 리턴 = 최대 중에 최소 찾기

        #특이 케이스 처리
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        citation_order = sorted(citations, reverse=True)
        answer = 0
        print(citation_order)
        for i in range(len(citations)):
            if citation_order[i] >= i+1:
                answer += 1
        return answer
