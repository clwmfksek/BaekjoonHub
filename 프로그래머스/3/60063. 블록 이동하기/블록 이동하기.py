from collections import deque


def solution(board):
    N = len(board)
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue = deque([(0, 0, 1, 0)])
    visited = set([(0, 0, 1)])

    while queue:
        r1, c1, dirc, mv = queue.popleft()
        r2, c2 = r1 + dx[dirc], c1 + dy[dirc]

        if r2 == N - 1 and c2 == N - 1:
            return mv

        for d in range(4):
            nx1, ny1 = r1 + dx[d], c1 + dy[d]
            nx2, ny2 = r2 + dx[d], c2 + dy[d]

            if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                if (nx1, ny1, dirc) in visited or board[nx1][ny1] == 1 or board[nx2][ny2] == 1: continue

                queue.append((nx1, ny1, dirc, mv + 1))
                visited.add((nx1, ny1, dirc))

                rotated_d = dirc ^ 1
                if dirc + d == 1:
                    if (r1, c1, rotated_d) not in visited:
                        queue.append((r1, c1, rotated_d, mv + 1))
                        visited.add((r1, c1, rotated_d))
                    if (r2, c2, rotated_d) not in visited:
                        queue.append((r2, c2, rotated_d, mv + 1))
                        visited.add((r2, c2, rotated_d))
                elif dirc + d == 3:
                    if (nx1, ny1, rotated_d) not in visited:
                        queue.append((nx1, ny1, rotated_d, mv + 1))
                        visited.add((nx1, ny1, rotated_d))
                    if (nx2, ny2, rotated_d) not in visited:
                        queue.append((nx2, ny2, rotated_d, mv + 1))
                        visited.add((nx2, ny2, rotated_d))

    return -1