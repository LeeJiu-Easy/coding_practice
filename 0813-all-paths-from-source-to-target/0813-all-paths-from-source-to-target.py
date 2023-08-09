class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque
        q = deque([(0, [])])
        answer = []
        while q:
            cur_node, path = q.popleft()
            if cur_node == len(graph)-1:
                answer.append(path + [cur_node])

            for node in graph[cur_node]:
                q.append((node, path + [cur_node]))
        return answer