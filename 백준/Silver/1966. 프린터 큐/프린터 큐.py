from collections import deque
t = int(input())

def maxx(lis):
	max_value = 0
	for i in lis:
		if i>max_value:
			max_value = i
	return max_value

def isempty(lis):
	if(lis): return 1
	else: return 0

for _ in range(t):
	count = 1
	a,b = map(int,input().split())
	lis = list(map(int,input().split()))
	queue = deque(lis)
	queue2 = deque([i for i in range(a)])

	while True:
		if not queue: break

		temp1 = queue.popleft()
		temp2 = queue2.popleft()
		if temp1 < maxx(queue):
			queue.append(temp1)
			queue2.append(temp2)
		else :
			if temp2 == b:
				print(count)
			count += 1