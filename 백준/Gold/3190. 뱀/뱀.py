import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) 
graph = [[0] * (n+1) for i in range(n+1)] 
k = int(input())
for i in range(k):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1

l = int(input())
tar = []
for i in range(l):
    m1, m2 = input().rstrip().split()
    m1 = int(m1)
    tar.append([m1, m2]) 

dx,dy = [1,0,-1,0], [0,1,0,-1]

count = 0 
queue = deque()
queue.append([1, 1]) 
x, y = 1, 1
dirc = 0  # 처음에는 동쪽을 바라봄
graph[y][x] = 2  # 뱀의 몸

while True:
    nx, ny = x + dx[dirc], y + dy[dirc]
    
    # 벽에 부딪히거나 자기 자신의 몸에 부딪히는 경우
    if nx <= 0 or ny <= 0 or nx > n or ny > n or [nx, ny] in queue:
        break
    
    # 사과가 없다면 꼬리 제거
    if graph[ny][nx] != 1:
        tail_x, tail_y = queue.popleft()
        graph[tail_y][tail_x] = 0  # 꼬리 부분을 지움
    
    # 새로운 위치로 이동
    graph[ny][nx] = 2
    queue.append([nx, ny])
    
    count += 1
    
    # 방향 변환 정보 확인
    if tar and count == tar[0][0]:
        if tar[0][1] == "D":  # 오른쪽으로 90도 회전
            dirc = (dirc + 1) % 4
        else:  # 왼쪽으로 90도 회전
            dirc = (dirc - 1) % 4
        tar.pop(0)  # 사용한 방향 변환 정보 삭제

    # 현재 위치 갱신
    x, y = nx, ny

# 결과 출력
print(count + 1)