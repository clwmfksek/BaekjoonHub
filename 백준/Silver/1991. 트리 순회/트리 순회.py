import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

tree = {}
lis = []
n = int(input())
for _ in range(n):
    item,left,right = map(str,input().strip().split())
    tree[item] = [left,item,right]
    lis.append(item)

def preorder(item):
    if item != '.':
        print(tree[item][1],end='')
        preorder(tree[item][0])
        preorder(tree[item][2])

def inorder(item):
    if item != '.':
        inorder(tree[item][0])
        print(tree[item][1],end='')
        inorder(tree[item][2])

def postorder(item):
    if item != '.':
        postorder(tree[item][0])
        postorder(tree[item][2])
        print(tree[item][1],end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')