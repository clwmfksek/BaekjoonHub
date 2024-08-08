import sys
input = sys.stdin.readline

def init(start,end,node):
    if start==end :
        seg_tree[node] = nums[start]
        return seg_tree[node]
    mid = (start+end)//2
    seg_tree[node] = init(start,mid,node*2) + init(mid+1,end,node*2+1)
    return seg_tree[node]

def query(left,right,node,start,end):
    if left > end or right < start : return 0
    if left <= start and end <= right : return seg_tree[node]
    mid = (start+end)//2
    return query(left,right,node*2,start,mid) + query(left,right,node*2+1,mid+1,end)

def update(start,end,node,ind,val):
    if start == end :
        seg_tree[node] = val
        return
    mid = (start+end)//2
    if ind <= mid :
        update(start,mid,node*2,ind,val)
    else:
        update(mid+1,end,node*2+1,ind,val)
    seg_tree[node] = seg_tree[node*2] + seg_tree[node*2+1]

N,Q = map(int,input().split())
nums = list(map(int,input().split()))
seg_tree = [0] + [0] * N*4

init(0,N-1,1)
for i in range(Q):
    x,y,a,b = map(int,input().split())
    if x > y :
        print(query(y-1,x-1,1,0,N-1))
    else :
        print(query(x-1,y-1,1,0,N-1))
    update(0,N-1,1,a-1,b)