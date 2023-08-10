class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque

        move_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        answer = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    q = deque([(i, j)])
                    grid[i][j] = 0  # 현재 노드를 방문했다고 표시
                    cnt = 0

                    while q:
                        cur_x, cur_y = q.popleft()
                        cnt += 1

                        for move in move_directions:
                            new_x = cur_x + move[0]
                            new_y = cur_y + move[1]

                            if (
                                0 <= new_x < len(grid)
                                and 0 <= new_y < len(grid[0])
                                and grid[new_x][new_y] == 1
                            ):
                                grid[new_x][new_y] = 0  # 방문한 노드는 0으로 표시
                                q.append((new_x, new_y))

                    answer = max(answer, cnt)

        return answer