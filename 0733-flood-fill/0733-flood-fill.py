class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque
        src_color = image[sr][sc]
        q = deque([(sr, sc)])
        visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        #up(0,x), down(len-1,x), left(x,0), right(x,len-1)

        while q:
            cur_x, cur_y = q.popleft()
            # 꺼내온 좌표가 이미 방문한 좌표인지 아닌지 체크
            if (cur_x, cur_y) in visited:
                continue

            elif image[cur_x][cur_y] == src_color:
                image[cur_x][cur_y] = color

            for move in moves:
                if move == moves[0] and cur_x == 0:
                    continue
                elif move == moves[1] and cur_x == len(image)-1:
                    continue
                elif move == moves[2] and cur_y == 0:
                    continue
                elif move == moves[3] and cur_y == len(image[0])-1:
                    continue
            
                
                new_x = cur_x + move[0]
                new_y = cur_y + move[1]
                
                if image[new_x][new_y] == src_color:
                    q.append((new_x, new_y))
                # 이동할 좌표 계산, 이동 가능한지 체크하고, 큐에 넣어줌
            
            visited.add((cur_x, cur_y))
        return image