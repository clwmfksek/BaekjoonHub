import sys
input = sys.stdin.readline

def update(start,end,node,idx,val):
    if start == end :
        seg_tree[node] = val
        return seg_tree[node]
    mid = (start+end)//2
    if idx <= mid:
        update(start,mid,node*2,idx,val)
    else :
        update(mid+1,end,node*2+1,idx,val)
    
    seg_tree[node] = max(seg_tree[node*2],seg_tree[node*2+1])
    return seg_tree[node]

def query(left,right,node,start,end):
    if left > end or right < start : return 0
    if left <= start and end <= right : return seg_tree[node]

    mid = (start+end)//2
    return max(query(left,right,node*2,start,mid),query(left,right,node*2+1,mid+1,end))

n,m = map(int,input().split())
nums = list(map(int,input().split()))

seg_tree = [0] * n * 4

for i in range(n):
    update(0,n-1,1,i,nums[i])
ans = []
for i in range(m-1,n-m+1):
    ans.append(query(i-(m-1),i+(m-1),1,0,n-1))

print(*ans)