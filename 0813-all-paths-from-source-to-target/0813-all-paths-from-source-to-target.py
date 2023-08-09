class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque

        q = deque([(graph[0], [0])])
        answer = []
        
        while q:
            cur, path = q.popleft()

            for pos in cur:
                new_path = path + [pos]
                q.append((graph[pos], new_path))
                if pos == len(graph)-1:
                    answer.append(new_path)

        return answer