import sys
input = sys.stdin.readline

color = list(map(int,input().split()))
count = 0

for i in range(3):
    count += color[i]//3 
    color[i] %= 3

while(color[0] and color[1] and color[2]):
    count += 1
    for i in range(3):
        color[i] -= 1

while(color[1] and color[2]):
    count += 1
    color[2] -= 1
    color[1] -= 1

while(color[0] and color[1]):
    count += 1
    color[0] -= 1
    color[1] -= 1

while(color[0] and color[2]):
    count += 1
    color[0] -= 1
    color[2] -= 1

for i in range(3):
    if color[i] : count += 1
print(count)