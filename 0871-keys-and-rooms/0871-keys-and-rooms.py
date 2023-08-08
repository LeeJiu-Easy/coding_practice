class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        
        q = deque([(rooms[0],0)])
        visited = set()

        while q:
            keys, pos = q.popleft()
            visited.add(pos)

            for key in keys:
                if not key in visited:
                    new_pos = key
                    q.append((rooms[key], new_pos))

        if len(visited) == len(rooms):
            answer = 1
        else:
            answer = 0
        return answer