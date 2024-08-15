import sys
input = sys.stdin.readline

def init(start,end,node):
    if start == end :
        seg_tree[node] = [nums[start],nums[start]]
        return seg_tree[node]
    mid = (start+end)//2
    left = init(start,mid,node*2)
    right = init(mid+1,end,node*2+1)
    maxvalue = max(left[0],right[0])
    minvalue = min(left[1],right[1])
    seg_tree[node] = [maxvalue,minvalue]
    return seg_tree[node]

def query(start,end,node,left,right):
    if left > end or right < start : return [-sys.maxsize,sys.maxsize]
    if left <= start and end <= right : return seg_tree[node]
    
    mid = (start+end)//2
    leftq = query(start,mid,node*2,left,right)
    rightq = query(mid+1,end,node*2+1,left,right)
    maxvalue = max(leftq[0],rightq[0])
    minvalue = min(leftq[1],rightq[1])
    return [maxvalue,minvalue]

n,q = map(int,input().split())
nums = []

for i in range(n):
    nums.append(int(input()))
seg_tree = [[-sys.maxsize,sys.maxsize] for i in range(n*4)] 
init(0,n-1,1)

for i in range(q):
    n1,n2 = map(int,input().split())
    result = query(0,n-1,1,n1-1,n2-1)
    print(result[0]-result[1])