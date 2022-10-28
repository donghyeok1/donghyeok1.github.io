from collections import deque

def solution(r, delivery):
    answer = 0
    graph = []
    for i in range(r):
        graph.append(delivery[3 * i : 3 * i + r])
    
    visited = [[False for _ in range(r)] for _ in range(r)]

    max_time = 0
    for i in range(r):
        for j in range(r):
            if max_time < graph[i][j][0]:
                max_time = graph[i][j][0]
    q = deque()

    x, y, time, tip = 0, 0, 0, graph[0][0][0]
    visited[0][0] = True
    q.append((x, y, time, tip, visited))
    while q:
        q_x, q_y, q_time, q_tip, q_vis = q.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = q_x + dx[i]
            ny = q_y + dy[i]

            if 0 <= nx < r and 0 <= ny < r:
                if q_time < max_time:
                    if q_vis[nx][ny]:
                        q.append((nx, ny, q_time + 1, q_tip, q_vis))
                    else:
                        q_vis[nx][ny] = True
                        if q_time <= graph[nx][ny][0]:
                            q_tip += graph[nx][ny][1]
                        q.append((nx, ny, q_time + 1, q_tip, q_vis))
                elif q_time == max_time:
                    if q_tip > answer:
                        answer = q_tip
                        

    return answer

print(solution(3, [[1,5],[8,3],[4,2],[2,3],[3,1],[3,2],[4,2],[5,2],[4,1]]))
# print(solution(4, [[1,10],[8,1],[8,1],[3,100],[8,1],[8,1],[8,1],[8,1],[8,1],[8,1],[8,1],[8,1],[9,100],[8,1],[8,1],[8,1]]))