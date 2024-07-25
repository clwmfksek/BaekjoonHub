import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().rstrip()

for i in alpha :
    word = word.replace(i, '_')  # input 변수와 동일한 이름의 변수
print(len(word))